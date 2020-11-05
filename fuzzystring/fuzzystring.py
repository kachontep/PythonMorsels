class FuzzyString:
    def __init__(self, val):
        self._val = val

    def __repr__(self):
        return repr(self._val)

    def __str__(self):
        return self._val

    def __eq__(self, other):
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        else:
            return str(self).lower() == str(other).lower()
