import cmath
import math
from decimal import Decimal
from typing import Union


def is_perfect_square(n: Union[int, float, Decimal, complex], *, complex: bool = False) -> bool:
    return PerfectSquare(complex).check(n)


class PerfectSquare:
    def __init__(self, complex_):
        if complex_:
            self._check = self._check_complex_num
        else:
            self._check = self._check_decimal_num

    def check(self, n):
        return self._check(n)

    def _check_int_num(self, n):
        return int(math.ceil(n)) - int(math.floor(n)) == 0

    def _check_complex_num(self, c):
        sqrt_n = cmath.sqrt(c)
        real_int = self._check_int_num(sqrt_n.real)
        imag_int = self._check_int_num(sqrt_n.imag)
        result = real_int and imag_int
        return result

    def _check_decimal_num(self, n):
        if not isinstance(n, (int, float, Decimal)):
            raise TypeError(
                "Unsupported types: int, float, Decimal and complex types are allowed")
        n = Decimal(str(n))
        if n < Decimal('0'):
            return False
        sqrt_n = int(n.sqrt())
        powered_sqrt_n = Decimal(sqrt_n ** 2)
        result = n == powered_sqrt_n
        return result
