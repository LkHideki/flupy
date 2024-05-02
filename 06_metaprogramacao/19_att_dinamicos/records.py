""" Este módulo tem as definições de Record
"""

import json, shelve


class Record:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)  # modo fácil de criar atributos

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__


class DbRecord(Record): ...


class Event(DbRecord): ...


def load_db(db: shelve.Shelf):
    with open("./osconfeed.json", "r") as data:
        j = json.load(data)
        for collection, rec_list in j["Schedule"].items():
            record_type = collection[:-1]
            for record in rec_list:
                key = f'{record_type}.{record["serial"]}'
                record["serial"] = key
                db[key] = Record(**record)
