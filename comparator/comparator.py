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

    def _check_delta(self, other):
        return abs(other - self._val) <= self._delta

    def __repr__(self):
        return f"Comparator({repr(self._val)}, delta={repr(self._delta)})"

    def __str__(self):
        return repr(self)
