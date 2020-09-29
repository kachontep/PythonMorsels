class SliceView:
    def __init__(self, sequence, start=None, stop=None, step=1):
        self._sequence = sequence
        self._start = start
        self._stop = stop
        self._step = step

    def _slice(self):
        slice_ = slice(self._start, self._stop, self._step)
        indices = slice_.indices(len(self._sequence))
        return indices

    def __len__(self):
        return len(range(*self._slice()))

    def __iter__(self):
        return (self._sequence[i] for i in range(*self._slice()))

    def __getitem__(self, key):
        if isinstance(key, slice):
            return SliceView(self._sequence, key.start, key.stop, key.step)
        elif isinstance(key, int):
            return self._sequence[range(*self._slice())[key]]
        else:
            raise TypeError("index must be int or slice")

