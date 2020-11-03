import functools


class PiecewiseRange:
    def __init__(self, ranges: str):
        self._ranges = PiecewiseRange.shrink_ranges(ranges)
        self._subranges = PiecewiseRange.parse_ranges(self._ranges)

    def __iter__(self):
        yield from self._iter_items()

    def __len__(self):
        return sum([len(subrange) for subrange in self._subranges])

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError("index should be int type")
        key = key < 0 and len(self) + key or key
        pos = 0
        for subrange in self._subranges:
            if pos + len(subrange) > key:
                return subrange[key - pos]
            pos += len(subrange)
        raise IndexError(f"{key} not found")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._ranges}')"

    def __eq__(self, other):
        if not isinstance(other, PiecewiseRange):
            return False
        elif other is self:
            return True
        else:
            return self._ranges == other._ranges

    def _iter_items(self):
        return functools.reduce(lambda acc, i: acc + list(i), self._subranges, [])

    @staticmethod
    def parse_inputs(inputs):
        return [s.strip() for s in inputs.split(",")]

    @staticmethod
    def parse_ranges(range_inputs):
        inputs = PiecewiseRange.parse_inputs(range_inputs)
        subranges = [PiecewiseRange.parse_pattern(input) for input in inputs]
        return subranges

    @staticmethod
    def shrink_ranges(range_inputs):
        inputs = PiecewiseRange.parse_inputs(range_inputs)

        def range_min_max(input):
            if "-" in input:
                vals = input.split("-")
                return int(vals[0]), int(vals[1])
            else:
                return int(input), int(input)

        def group_range(items, input):
            if items:
                prev_min, prev_max = range_min_max(items[-1])
                curr_min, curr_max = range_min_max(input)
                if curr_min - prev_max == 1:
                    return items[:-1] + [f"{prev_min}-{curr_max}"]
                else:
                    return items + [input]
            else:
                return [input]

        items = functools.reduce(group_range, inputs, [])
        shrinked = ",".join(items)
        return shrinked

    @staticmethod
    def parse_pattern(pattern):
        result = None
        if "-" in pattern:
            start, stop = pattern.split("-")
            result = range(int(start), int(stop) + 1)
        else:
            result = [int(pattern)]
        return result
