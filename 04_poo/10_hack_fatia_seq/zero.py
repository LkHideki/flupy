''' Classe Vetor versionada
'''

from array import array
from functools import reduce
from itertools import chain
import numbers
import operator
import reprlib
import math
from typing import Any

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
            cls = type(self)
            if isinstance(i, slice):
                return cls(self._components[i])
            elif isinstance(i, numbers.Integral):
                return self._components[i]
            msg = f'{cls.__name__}: os índices devem ser números inteiros.'
            raise TypeError(msg)

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

class Tomada3:
    class Vetor:
        typecode = "d"
        shortcuts = 'xyzw'

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
            cls = type(self)
            if isinstance(i, slice):
                return cls(self._components[i])
            elif isinstance(i, numbers.Integral):
                return self._components[i]
            msg = f'{cls.__name__}: os índices devem ser números inteiros.'
            raise TypeError(msg)

        def __getattr__(self, attr: str):
            cls = type(self)
            if len(attr) == 1:
                i = cls.shortcuts.find(attr)
                if 0 <= i < len(self._components):
                    return self._components[i]
            msg = f"{cls.__name__} não tem atributo {attr}"
            raise AttributeError(msg)

        def __setattr__(self, name, value) -> None:
            cls = type(self)
            if len(name) == 1:
                error = ''
                if name in cls.shortcuts:
                    error = f'O atributo {name} é readonly.'
                elif name.islower():
                    error = f'Não é possível setar atributos de a a z em {cls.__name__}'

                if error:
                    raise AttributeError(error)
            super().__setattr__(name, value)

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

class Tomada4:
    class Vetor:
        typecode = "d"
        shortcuts = 'xyzw'

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

        def __eq__(self, other) -> bool:
            if len(self) != len(other): return False
            return all(a == b for a, b in zip(self, other))

        def __hash__(self) -> int:
            # hashes = (hash(x) for x in self._components)
            hashes = map(hash, self._components)
            return reduce(operator.xor, hashes, 0)

        def __abs__(self) -> float:
            return math.sqrt(sum(x * x for x in self))

        def __bool__(self) -> bool:
            return bool(abs(self))

        def __len__(self) -> int:
            return len(self._components)

        def __getitem__(self, i: int):
            cls = type(self)
            if isinstance(i, slice):
                return cls(self._components[i])
            elif isinstance(i, numbers.Integral):
                return self._components[i]
            msg = f'{cls.__name__}: os índices devem ser números inteiros.'
            raise TypeError(msg)

        def __getattr__(self, attr: str):
            cls = type(self)
            if len(attr) == 1:
                i = cls.shortcuts.find(attr)
                if 0 <= i < len(self._components):
                    return self._components[i]
            msg = f"{cls.__name__} não tem atributo {attr}"
            raise AttributeError(msg)

        def __setattr__(self, name, value) -> None:
            cls = type(self)
            if len(name) == 1:
                error = ''
                if name in cls.shortcuts:
                    error = f'O atributo {name} é readonly.'
                elif name.islower():
                    error = f'Não é possível setar atributos de a a z em {cls.__name__}'

                if error:
                    raise AttributeError(error)
            super().__setattr__(name, value)

        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)

class Tomada5:
    class Vetor:
        typecode = "d"
        shortcuts = 'xyzw'

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

        def __eq__(self, other) -> bool:
            if len(self) != len(other): return False
            return all(a == b for a, b in zip(self, other))

        def __hash__(self) -> int:
            # hashes = (hash(x) for x in self._components)
            hashes = map(hash, self._components)
            return reduce(operator.xor, hashes, 0)

        def __abs__(self) -> float:
            return math.sqrt(sum(x * x for x in self))

        def __bool__(self) -> bool:
            return bool(abs(self))

        def __len__(self) -> int:
            return len(self._components)

        def __getitem__(self, i: int):
            cls = type(self)
            if isinstance(i, slice):
                return cls(self._components[i])
            elif isinstance(i, numbers.Integral):
                return self._components[i]
            msg = f'{cls.__name__}: os índices devem ser números inteiros.'
            raise TypeError(msg)

        def __getattr__(self, attr: str):
            cls = type(self)
            if len(attr) == 1:
                i = cls.shortcuts.find(attr)
                if 0 <= i < len(self._components):
                    return self._components[i]
            msg = f"{cls.__name__} não tem atributo {attr}"
            raise AttributeError(msg)

        def __setattr__(self, name, value) -> None:
            cls = type(self)
            if len(name) == 1:
                error = ''
                if name in cls.shortcuts:
                    error = f'O atributo {name} é readonly.'
                elif name.islower():
                    error = f'Não é possível setar atributos de a a z em {cls.__name__}'

                if error:
                    raise AttributeError(error)
            super().__setattr__(name, value)

        def angle(self, n: int):
            r = math.sqrt(sum(x*x for x in self._components[n:]))
            a = math.atan2(r, self[n-1])
            if (n == len(self) - 1) and self[-1] < 0:
                return math.pi * 2 - a
            return a

        def angles(self):
            return (self.angle(n) for n in range(1, len(self)))
        
        def __format__(self, format_spec: str = '') -> str:
            if format_spec.endswith('h'):
                format_spec = format_spec[:-1]
                coords: Any = chain([abs(self)], self.angles())
                outer_fmt = '<{}>'
            else:
                coords = self
                outer_fmt = "({})"
            components = (format(c, format_spec) for c in coords)
            return outer_fmt.format(', '.join(components))
        
        @classmethod
        def frombytes(cls, octets):
            typecode = chr(octets[0])
            memv = memoryview(octets[1:]).cast(typecode)
            return cls(memv)


