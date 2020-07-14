from collections.abc import Iterable


def deep_flatten(ll):
    if not isinstance(ll, Iterable) \
            or isinstance(ll, (str, bytes)):
        yield ll
    else:
        for e in ll:
            yield from deep_flatten(e)
