class RomanNumeral:
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

    def __init__(self, roman: str):
        self._roman = roman
        self._int = self.__class__.from_num(self._roman)

    @classmethod
    def from_num(cls, roman: str) -> int:
        total = 0
        i_ = None
        try:
            for i in range(len(roman)):
                i_ = i
                value = cls.ints[cls.nums.index(roman[i])]
                try:
                    nextvalue = cls.ints[cls.nums.index(roman[i + 1])]
                    if nextvalue > value:
                        value *= -1
                except IndexError:
                    pass
                total += value
        except ValueError:
            raise ValueError("Invalid Roman character '{}'".format(roman[i_]))
        if total == 0:
            raise ValueError("Roman didn't have zero value")
        return total

    @classmethod
    def from_int(cls, value: int) -> str:
        value_ = value
        pos = 0
        s = []
        while value_ > 0 and pos < len(cls.nums):
            if value_ >= cls.ints[pos]:
                n = value_ // cls.ints[pos]
                s.append(cls.nums[pos] * n)
                value_ -= cls.ints[pos] * n
            pos += 1
        r = "".join(s)
        return r

    def __int__(self):
        return self.__class__.from_num(self._roman)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._roman}')"

    def __str__(self):
        return self._roman

    def __add__(self, other):
        cls = self.__class__
        if isinstance(other, int):
            return cls(cls.from_int(self._int + other))
        elif isinstance(other, RomanNumeral):
            return cls(cls.from_int(self._int + other._int))
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self._int < other._int
        elif isinstance(other, int):
            return self._int < other
        elif isinstance(other, str):
            raise TypeError("Inequality/equality supports in str")
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self._int == other._int
        elif isinstance(other, int):
            return self._int == other
        elif isinstance(other, str):
            return str(self) == other
        return NotImplemented

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        return not (self < other or self == other)

    def __le__(self, other):
        return not self > other

