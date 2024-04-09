''' Classe Vetor versionada
'''

from array import array
import reprlib
import math

class Tomada1:
    class Vetor:
        typecode = "d"

        def __init__(self, components) -> None:
            self._components = array(self.typecode, components)

        def __iter__(self):
            return iter(self._components)

        def __repr__(self) -> str:
            components = reprlib.repr(self._components)
            components = components[components.find("[") : -1]
            return f"Vetor({components})"

        def __str__(self) -> str:
            return str(tuple(self))

        def __bytes__(self) -> bytes:
            tc = bytes([ord(self.typecode)])
            comp = bytes(self._components)
            return tc + comp

        def __eq__(self, value) -> bool:
            return tuple(self) == tuple(value)

        def __abs__(self) -> float:
            return math.sqrt(sum(x * x for x in self))

        def __bool__(self) -> bool:
            return bool(abs(self))

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

class Tomada2:
    class Vetor:
        typecode = "d"

        def __init__(self, components) -> None:
            self._components = array(self.typecode, components)

        def __iter__(self):
            return iter(self._components)

        def __repr__(self) -> str:
            components = reprlib.repr(self._components)
            components = components[components.find("[") : -1]
            return f"Vetor({components})"

        def __str__(self) -> str:
            return str(tuple(self))

        def __bytes__(self) -> bytes:
            tc = bytes([ord(self.typecode)])
            comp = bytes(self._components)
            return tc + comp

        def __eq__(self, value) -> bool:
            return tuple(self) == tuple(value)

        def __abs__(self) -> float:
            return math.sqrt(sum(x * x for x in self))

        def __bool__(self) -> bool:
            return bool(abs(self))

        def __len__(self) -> int:
            return len(self._components)

        def __getitem__(self, i: int):
            return self._components[i]

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)