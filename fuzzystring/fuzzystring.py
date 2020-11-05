import unicodedata


class FuzzyString:
    def __init__(self, val):
        self._val = val

    @staticmethod
    def _validate_types(other):
        return isinstance(other, (str, FuzzyString))

    @staticmethod
    def _normalize(val):
        return unicodedata.normalize("NFKD", str(val).casefold())

    def __repr__(self):
        return repr(self._val)

    def __str__(self):
        return self._val

    def __eq__(self, other):
        if self._validate_types(other):
            return self._normalize(self) == self._normalize(other)
        return NotImplemented

    def __lt__(self, other):
        if self._validate_types(other):
            return self._normalize(self) < self._normalize(other)
        return NotImplemented

    def __ge__(self, other):
        return not (self < other)

    def __gt__(self, other):
        if self._validate_types(other):
            return self._normalize(self) > self._normalize(other)
        return NotImplemented

    def __le__(self, other):
        return not (self > other)

    def __contains__(self, member):
        if self._validate_types(member):
            return self._normalize(member) in self._normalize(self)
        return NotImplemented

    def __add__(self, other):
        if self._validate_types(other):
            return FuzzyString(str(self) + str(other))
        return NotImplemented
