import abc


class AutoStorage:
    __counter = 0

    def __init__(self) -> None:
        cls = self.__class__
        self.storage_name = f"_{cls.__counter}@{cls.__name__}"
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """Devolve o valor validado ou levanta ValueError"""

class Quantity(Validated):
    """É um número maior do que zero"""

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("O valor deve ser positivo!")
        return value

class NonBlank(Validated):
    """Uma string com pelo menos um caractere não-branco."""

    def validate(self, instance, value: str):
        _value = value.strip()
        if len(_value) == 0:
            raise ValueError("O valor não pode estar em branco")
        return _value



if __name__ == "__main__":
    pass
