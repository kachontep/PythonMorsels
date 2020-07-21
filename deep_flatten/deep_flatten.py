from collections.abc import Iterable


def deep_flatten(ll):
    if not is_iterable(ll):
        yield ll
    elif is_string(ll):
        yield ll
    else:
        for e in ll:
            yield from deep_flatten(e)


def is_iterable(ll):
    return isinstance(ll, Iterable)


def is_string(ll):
    return isinstance(ll, (str, bytes))
