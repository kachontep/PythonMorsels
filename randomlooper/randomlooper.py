import random


def RandomLooper(seq):
    choices = list(seq)
    while choices:
        chosen = random.randint(0, len(choices) - 1)
        yield choices[chosen]
        choices.pop(chosen)
