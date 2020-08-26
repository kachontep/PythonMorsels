from datetime import date
from decimal import Decimal
from typing import Iterable, Tuple, NamedTuple, Set, List


class RTrans(NamedTuple):
    trans_date: str
    department: str
    amount: str
    payee: str


class RTransResult(NamedTuple):
    trans_date: str
    department: str
    amount: str
    payee: str
    result: str


def make_trans_tuple(trans: Iterable[List]) -> Iterable[RTrans]:
    return [RTrans(*tran) for tran in trans]


def make_trans_result(trans: Iterable[RTrans], shared: Set[RTrans]) -> Iterable[RTransResult]:
    return [list(RTransResult(*tran, 'FOUND' if tran in shared else 'MISSING')) for tran in trans]


def reconcile_accounts(trans1: Iterable[List], trans2: Iterable[List]) -> Tuple[Iterable[RTransResult], Iterable[RTransResult]]:
    ttrans1 = make_trans_tuple(trans1)
    ttrans2 = make_trans_tuple(trans2)
    shared = set(ttrans1).intersection(set(ttrans2))
    output1 = make_trans_result(ttrans1, shared)
    output2 = make_trans_result(ttrans2, shared)
    return output1, output2
