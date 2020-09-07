from collections import defaultdict
from datetime import datetime
from typing import Iterable, Tuple, NamedTuple, Set, List, Dict


class Transaction(NamedTuple):
    trans_date: str
    department: str
    amount: str
    payee: str


def sort_tx_with_idx(transactions: Iterable[Tuple[int, Transaction]]):
    return sorted(transactions, key=lambda r: r[1].trans_date)


def match_transactions(trans: Transaction, trans_list: Iterable[Transaction]) -> List[Tuple[int, Transaction]]:
    """
    Match a transaction with closest transactions in the transaction list
    The return reseult will be sorted in earliest time.
    :param tran: a transation to search for
    :param tran_list: list of transactiont to search for the closest
    :return:
    """
    trans_date = datetime.strptime(trans.trans_date, '%Y-%m-%d')

    result = []
    for idx, tx in trans_list:
        tx_date = datetime.strptime(tx.trans_date, '%Y-%m-%d')
        date_diff = abs(trans_date - tx_date)
        if date_diff.days <= 1 and trans[1:] == tx[1:]:
            result.append((idx, tx))

    result = sort_tx_with_idx(result)
    return result


def reconcile_accounts(trans1: Iterable[List[str]], trans2: Iterable[List[str]]):
    ttrans1 = list(enumerate([Transaction(*trans) for trans in trans1]))
    ttrans2 = list(enumerate([Transaction(*trans) for trans in trans2]))
    trans1_search_txs = ttrans1[:]
    trans2_remain_txs = ttrans2[:]

    # Scan and matching process after the process
    # the matches in trans1 and remain unmatched in trans2
    # result are kept in trans1_match_txs and trans2_remain_txs
    # respectively.
    trans1_match_txs = []
    for idx, s_trans in sort_tx_with_idx(trans1_search_txs):
        matches = match_transactions(s_trans, trans2_remain_txs)
        if matches:
            trans1_match_txs.append((idx, s_trans))
            trans2_remain_txs.remove(matches[0])

    # Generate result for transaction in transaction1
    # list both found and missing
    output1 = [
        [*s_trans, (idx, s_trans) in trans1_match_txs and 'FOUND' or 'MISSING']
        for idx, s_trans in ttrans1
    ]

    # Generate result for transaction in transaction2 list
    # both found and missing
    output2 = [
        [*r_trans, (idx, r_trans) in trans2_remain_txs and 'MISSING' or 'FOUND']
        for idx, r_trans in ttrans2
    ]

    return output1, output2
