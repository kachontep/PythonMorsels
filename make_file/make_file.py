import random
from contextlib import contextmanager
from os import unlink
from pathlib import Path

CHARACTERS = (
    [chr(ord('a') + i) for i in range(26)] +
    [chr(ord('A') + i) for i in range(26)] +
    ['_', '=']
)


def random_file_length():
    return random.randint(3, 21)


def random_file_name(k):
    return ''.join(random.choices(CHARACTERS, k=k))


def temp_file_name():
    return random_file_name(random_file_length())


@contextmanager
def make_file():
    file_name = temp_file_name()
    f = Path(file_name)
    f.touch()
    try:
        yield file_name
    finally:
        if f.exists():
            f.unlink()
