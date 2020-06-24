from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Vector:
    x: Any
    y: Any
    z: Any

    __slots__ = ('x', 'y', 'z')

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __str__(self):
        return repr(self)

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    def __eq__(self, other):
        if other is self:
            return True
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported + operator for " + type(other))
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported - operator for " + type(other))
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Unsupported * operator for " + type(other))
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1/other)
