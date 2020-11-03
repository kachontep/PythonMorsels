from contextlib import contextmanager


class Comparator:

    _default_delta = 1e-7

    def __init__(self, val, delta=None):
        self._val = val
        self._delta = delta or self.__class__._default_delta

    def _check_delta(self, other):
        return abs(other - self._val) <= self._delta

    def __eq__(self, other):
        if not isinstance(other, (int, float, Comparator)):
            return False
        elif other is self:
            return True
        else:
            return self._check_delta(other)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            val = self._val + other
            delta = self._delta
        elif isinstance(other, Comparator):
            val = self._val + other._val
            delta = max(self._delta, other._delta)
        else:
            raise TypeError("support only with int or float")
        return self.__class__(val, delta=delta)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -1 * other

    def __rsub__(self, other):
        return -1 * self + other

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float)):
            raise TypeError("support only with int or float")
        val = self._val * multiplier
        delta = self._delta
        return self.__class__(val, delta=delta)

    def __rmul__(self, other):
        return self * other

    def __repr__(self):
        return f"Comparator({repr(self._val)}, delta={repr(self._delta)})"

    def __str__(self):
        return repr(self)

    @classmethod
    def default_delta(cls, delta):
        @contextmanager
        def contextmanager_factory():
            _default_delta, cls._default_delta = cls._default_delta, delta
            try:
                yield
            finally:
                cls._default_delta = _default_delta

        return contextmanager_factory()
