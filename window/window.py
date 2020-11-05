import itertools


def window(iterable, size):
    items = []
    captured = False
    for e in iterable:
        items.append(e)
        if len(items) == size:
            captured = True
        if not captured:
            continue
        yield tuple(items)
        items = items[1:]
    if not captured:
        return [tuple(items) + ((None,) * (size - len(items)))]
