import random
from itertools import chain


class RandomLooper:
    def __init__(self, *args):
        self._choices = list(chain(*args))

    def __iter__(self):
        yield from self._rand_choices()

    def _rand_choices(self):
        choices = self._choices.copy()
        random.shuffle(choices)
        return choices

    def __len__(self):
        return len(self._choices)
