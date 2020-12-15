class ChainSequence:
    def __init__(self, *sequences):
        self._sequences = list(sequences)

    def __len__(self):
        return sum(len(s) for s in self._sequences)

    def __iter__(self):
        return (x for s in self._sequences for x in s)

    def __getitem__(self, key):
        if key < 0:
            key = len(self) + key
        pos = 0
        for s in self._sequences:
            if pos <= key < pos + len(s):
                return s[key - pos]
            pos += len(s)

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

    @property
    def sequences(self):
        return self._sequences