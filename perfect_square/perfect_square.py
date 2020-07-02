import math
from decimal import Decimal
from typing import Union


def is_perfect_square(n: Union[int, float, Decimal]) -> bool:
    if not isinstance(n, (int, float, Decimal)):
        raise TypeError("Unsupported whole number type")
    if n < 0:
        return False
    n = Decimal(str(n))
    sqrt_n = int(n.sqrt())
    powered_sqrt_n = Decimal(sqrt_n ** 2)
    return n == powered_sqrt_n
