from collections import defaultdict
from typing import Iterable, Tuple, NamedTuple, Set, List, Dict


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


def make_trans_result(trans: Iterable[RTrans], shared_trans_count: Dict[RTrans, int]) -> Iterable[RTransResult]:
    shared_trans_count = shared_trans_count.copy()
    result = []
    for tran in trans:
        if tran in shared_trans_count and shared_trans_count[tran] > 0:
            shared_trans_count[tran] -= 1
            found = True
        else:
            found = False
        result.append(
            list(RTransResult(*tran, 'FOUND' if found else 'MISSING')))
    return result


def max_shared_trans_count(trans1: Iterable[RTrans], trans2: Iterable[RTrans], shared_trans: Set[RTrans]) -> Dict[RTrans, int]:
    count1 = defaultdict(int)
    count2 = defaultdict(int)
    for tran in trans1:
        if tran in shared_trans:
            count1[tran] += 1
    for tran in trans2:
        if tran in shared_trans:
            count2[tran] += 1
    return {tran: min(count1[tran], count2[tran]) for tran in shared_trans}


def reconcile_accounts(trans1: Iterable[List], trans2: Iterable[List]) -> Tuple[Iterable[RTransResult], Iterable[RTransResult]]:
    ttrans1 = make_trans_tuple(trans1)
    ttrans2 = make_trans_tuple(trans2)
    shared_trans = set(ttrans1).intersection(set(ttrans2))
    shared_trans_count = max_shared_trans_count(ttrans1, ttrans2, shared_trans)
    output1 = make_trans_result(ttrans1, shared_trans_count)
    output2 = make_trans_result(ttrans2, shared_trans_count)
    return output1, output2
