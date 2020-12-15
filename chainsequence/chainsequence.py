class ChainSequence:

    class SliceView:
        def __init__(self, sequences, indices):
            self._sequences = sequences
            self._indices = indices

        def __iter__(self):
            return (self._sequences[index] for index in self._indices)

    def __init__(self, *sequences):
        self._sequences = list(sequences)

    def __len__(self):
        return sum(len(s) for s in self._sequences)

    def __iter__(self):
        return (x for s in self._sequences for x in s)

    def __getitem__(self, key):
        if isinstance(key , slice):
            indices = range(*key.indices(len(self)))
            return ChainSequence.SliceView(self, indices)
        return self._getitem(key)

    def __eq__(self, other):
        if other is self:
            return True
        if isinstance(other, ChainSequence):
            other_ = other.sequences
        else:
            other_ = other
        self_ = self._sequences
        if len(other_) != len(self_):
            return False
        return all(a == b for a, b in zip(other_, self_))

    def __add__(self, other):
        return ChainSequence(*self._append(other))

    def __iadd__(self, other):
        self._sequences = self._append(other)
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(s) for s in self._sequences)})"

    def _getitem(self, key):
        if key < 0:
            key = len(self) + key
        if key >= len(self):
            raise KeyError(f"{key} not in range")
        pos = 0
        for s in self._sequences:
            if pos <= key < pos + len(s):
                return s[key - pos]
            pos += len(s)

    def _append(self, sequence):
        return self._sequences + [sequence]

    @property
    def sequences(self):
        return self._sequences