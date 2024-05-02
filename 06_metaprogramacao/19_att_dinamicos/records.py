""" Este módulo tem as definições de Record
"""

import inspect
import json, shelve


class BancoDeDadosFaltandoError(RuntimeError):
    pass


class Record:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)  # modo fácil de criar atributos

    def __eq__(self, other) -> bool:
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        return NotImplemented


class DbRecord(Record):
    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                raise BancoDeDadosFaltandoError(
                    "Tá faltando o banco de dados. Execute o .set_db"
                )
            raise

    def __repr__(self):
        if hasattr(self, "serial"):
            clsname = self.__class__.__name__
            return f"<{clsname} serial={self.serial}>"
        return super().__repr__()


class Event(DbRecord):
    @property
    def venue(self):
        key = f"venue.{self.venue_serial}"
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, "_speaker_objs"):
            spkr_serials = self.__dict__["speakers"]
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch(f"speaker.{key}") for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, "name"):
            cls_name = self.__class__.__name__
            return f"<{cls_name} {self.name}>"
        return super().__repr__()


def load_db(db: shelve.Shelf):
    with open("./osconfeed.json", "r") as data:
        j = json.load(data)
        for collection, rec_list in j["Schedule"].items():
            record_type: str = collection[:-1]
            cls_name = record_type.capitalize()
            cls = globals().get(cls_name, DbRecord)

            if inspect.isclass(cls) and issubclass(cls, DbRecord):
                factory = cls
            else:
                factory = DbRecord

            for record in rec_list:
                key = f'{record_type}.{record["serial"]}'
                record["serial"] = key
                db[key] = factory(**record)
