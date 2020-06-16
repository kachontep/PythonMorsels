import math


class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"Circle({self.radius})"
