import random
from functools import reduce
from collections.abc import Iterable


class RandomLooper:
    def __init__(self, *args):
        for seq in args:
            if not isinstance(seq, Iterable):
                raise TypeError("Parameters should be iterable")
        self._choices = reduce(lambda acc, c: acc + list(c), args, [])

    def __iter__(self):
        yield from self._rand_choices()

    def _rand_choices(self):
        choices = self._choices.copy()
        random.shuffle(choices)
        return choices

    def __len__(self):
        return len(self._choices)
