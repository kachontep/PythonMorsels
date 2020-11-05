class FuzzyString:
    def __init__(self, val):
        self._val = val

    def _validate_types(self, other):
        return isinstance(other, (str, FuzzyString))

    def __repr__(self):
        return repr(self._val)

    def __str__(self):
        return self._val

    def __eq__(self, other):
        if self._validate_types(other):
            return str(self).lower() == str(other).lower()
        return NotImplemented

    def __lt__(self, other):
        if self._validate_types(other):
            return str(self).lower() < str(other).lower()
        return NotImplemented

    def __ge__(self, other):
        return not (self < other)

    def __gt__(self, other):
        if self._validate_types(other):
            return str(self).lower() > str(other).lower()
        return NotImplemented

    def __le__(self, other):
        return not (self > other)

    def __contains__(self, member):
        if self._validate_types(member):
            return member.lower() in str(self).lower()
        return NotImplemented

    def __add__(self, other):
        if self._validate_types(other):
            return FuzzyString(str(self) + str(other))
        return NotImplemented
