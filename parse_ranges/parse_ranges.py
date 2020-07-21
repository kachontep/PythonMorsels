import re
from itertools import chain
from typing import Iterable, Generator

RANGE_PATTERN = re.compile(r'\b(\d+)(-(\d+)|->(\w+))?\b')


def range_from_string(s: str) -> Generator[str, None, None]:
    match = RANGE_PATTERN.search(s, 0)
    while match:
        start, _, end, _ = match.groups()
        if end is None:
            end = start
        yield (int(start), int(end))
        match = RANGE_PATTERN.search(s, match.end() + 1)


def generate_range(start: int, end: int):
    return range(start, end+1)


def parse_ranges(rngs_str: str) -> Iterable[int]:
    rngs = [generate_range(start, end)
            for start, end in range_from_string(rngs_str)]
    result = chain(*rngs)
    return result
