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


make_file_options = {
    "mode": "wt",
}


@contextmanager
def make_file(contents=None, directory=None, **options):
    options = {**make_file_options, **options}
    d = Path(directory) if directory else Path.cwd()
    f = d / Path(temp_file_name())
    if not d.exists():
        d.mkdir()
    if not f.exists():
        f.touch()
    if contents:
        with f.open(**options) as h:
            h.write(contents)
    try:
        yield str(f)
    finally:
        if f.exists():
            f.unlink()
