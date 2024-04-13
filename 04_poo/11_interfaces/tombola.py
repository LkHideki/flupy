from abc import ABC, abstractmethod
from collections.abc import Iterable

class Tombola(ABC):
    @abstractmethod
    def load(self, iterable: Iterable): ...

    @abstractmethod
    def pick(self): ...

    def loaded(self) -> bool:
        return bool(self.inspect())
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))