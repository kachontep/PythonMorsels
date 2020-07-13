
SENTINEL = object()


def compact(seq):
    p = SENTINEL
    for q in seq:
        if p != q:
            yield q
        p = q
