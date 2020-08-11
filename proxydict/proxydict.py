from collections.abc import Mapping

sentinel = object()


class ProxyDict:
    def __init__(self, d=sentinel):
        # self._items = dict({} if d is sentinel else d)
        self._items = dict() if d is sentinel else d

    def __getitem__(self, key):
        return self._items[key]

    def __setitem__(self, key, value):
        raise TypeError(f"'{self.__class__.__name__}' does not support item assignment")

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        yield from self._items

    def __eq__(self, other):
        if other is self:
            return True
        elif isinstance(other, ProxyDict):
            return self._items == other._items
        elif isinstance(other, Mapping):
            return self._items == other
        else:
            return False

    def __repr__(self):
        return repr(self._items)

    def keys(self):
        return self._items.keys()

    def values(self):
        return self._items.values()

    def items(self):
        return self._items.items()
