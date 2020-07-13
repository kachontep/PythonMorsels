import numbers


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if other is None:
            return False
        if other is self:
            return True
        if isinstance(other, Point):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return other == self

    def __add__(self, other):
        if other is None or not isinstance(other, Point):
            raise TypeError(
                f"+ should be used with another Point instance rather than {other}")
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if other is None or not isinstance(other, Point):
            raise TypeError(
                f"- should be used with another Point instance rather than {other}")
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, n):
        if n is None or not isinstance(n, numbers.Number):
            raise TypeError(
                f"* should be used with another number rather than {n}")
        return Point(self.x * n, self.y * n, self.z * n)

    def __rmul__(self, n):
        return self * n

    def __iter__(self):
        yield from (self.x, self.y, self.z)
