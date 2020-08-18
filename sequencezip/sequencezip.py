class SequenceZip:
    def __init__(self, *seqargs):
        self._seqargs = seqargs

    def __iter__(self):
        yield from zip(*self._seqargs)

    def __len__(self):
        return min([len(seq) for seq in self._seqargs])
    
    def __getitem__(self, index):
        len_ = len(self)
        if isinstance(index, slice):
            return SequenceZip(*[seqarg[:len_][index] for seqarg in self._seqargs])
        else:
            index = index + len(self) if index < 0 else index   
            return tuple([seq[index] for seq in self._seqargs])

    def __repr__(self):
        return f'SequenceZip({", ".join([repr(seq) for seq in self._seqargs])})'

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, SequenceZip):
            return False
        elif len(self) == len(other):
            len_ = len(self)
            return all([ss[:len_] == os[:len_] for ss, os in zip(self._seqargs, other._seqargs)])
        else:
            return False