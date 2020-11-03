class Comparator:
    def __init__(self, val, delta=1e-7):
        self._val = val
        self._delta = delta

    def __eq__(self, other):
        if not isinstance(other, (int, float, Comparator)):
            return False
        elif other is self:
            return True
        else:
            return self._check_delta(other)

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("support only with int or float")
        return self.__class__(self._val + other, delta=self._delta)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -1 * other

    def __rsub__(self, other):
        return -1 * self + other

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("support only with int or float")
        return self.__class__(self._val * other, delta=self._delta)

    def __rmul__(self, other):
        return self * other

    def _check_delta(self, other):
        return abs(other - self._val) <= self._delta

    def __repr__(self):
        return f"Comparator({repr(self._val)}, delta={repr(self._delta)})"

    def __str__(self):
        return repr(self)
