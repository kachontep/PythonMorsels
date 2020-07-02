import cmath
import math
from decimal import Decimal
from typing import Union


def is_perfect_square(n: Union[int, float, Decimal, complex], *, complex: bool = False) -> bool:
    return PerfectSquare(n, complex).check()


class PerfectSquare:
    def __init__(self, n, complex):
        self.n = n
        self._check = self.check_decimal
        if complex:
            self._check = self.check_complex

    def check(self):
        return self._check(self.n)

    def _check_int(self, n):
        return int(math.ceil(n)) - int(math.floor(n)) == 0

    def check_complex(self, c):
        sqrt_n = cmath.sqrt(c)
        real_int = self._check_int(sqrt_n.real)
        imag_int = self._check_int(sqrt_n.imag)
        result = real_int and imag_int
        return result

    def check_decimal(self, n):
        if not isinstance(self.n, (int, float, Decimal)):
            raise TypeError(
                "Unsupported types: int, float, Decimal and complex types are allowed")
        n = Decimal(str(n))
        if n < Decimal('0'):
            return False
        sqrt_n = int(n.sqrt())
        powered_sqrt_n = Decimal(sqrt_n ** 2)
        result = n == powered_sqrt_n
        return result
