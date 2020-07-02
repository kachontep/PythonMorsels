import cmath
import math
from decimal import Decimal
from typing import Union


def _check_int(n: float) -> bool:
    return int(math.ceil(n)) - int(math.floor(n)) == 0


def _check_perfect_square(n: Decimal) -> bool:
    if n < Decimal('0'):
        return False
    sqrt_n = int(n.sqrt())
    powered_sqrt_n = Decimal(sqrt_n ** 2)
    return n == powered_sqrt_n


def _check_perfect_square_complex(c: complex) -> bool:
    sqrt_n = cmath.sqrt(c)
    real_int = _check_int(sqrt_n.real)
    imag_int = _check_int(sqrt_n.imag)
    return real_int and imag_int


def is_perfect_square(n: Union[int, float, Decimal, complex], *, complex: bool = False) -> bool:
    if complex == True:
        return _check_perfect_square_complex(n)
    if not isinstance(n, (int, float, Decimal)):
        raise TypeError("Support int, float, Decimand and complex types")
    return _check_perfect_square(Decimal(str(n)))
