from functools import reduce


def add(*args):

    def validate_size(m1, m2):
        row_unmatched = any([len(m1) != len(m2)])
        col_unmatched = any([len(r1) != len(r2) for r1, r2 in zip(m1, m2)])
        if row_unmatched or col_unmatched:
            raise ValueError("Given matrices are not the same size.")

    def matrix_add(m1, m2):
        validate_size(m1, m2)
        return [
            [c1 + c2 for (c1, c2) in zip(r1, r2)]
            for r1, r2 in zip(m1, m2)
        ]

    return reduce(matrix_add, args)
