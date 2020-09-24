import csv


class FancyReader:
    class Row:
        def __init__(self, **kwargs):
            self._kwargs = kwargs

        def __getattr__(self, key):
            return self._kwargs.get(key) or super().__getattr__(key)

        def __iter__(self):
            yield from self._kwargs.values()

        def __repr__(self):
            args = ["{}={}".format(k, repr(v)) for k, v in self._kwargs.items()]
            return f"Row({', '.join(args)})"

    def __init__(self, *args, fieldnames=None, **kwargs):
        self._fieldnames = fieldnames
        self._args = args
        self._kwargs = kwargs
        self._iterator = None
        self.line_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iterator is None:
            reader = csv.reader(*self._args, **self._kwargs)
            self._iterator = iter(reader)
            if not self._fieldnames:
                self._fieldnames = next(reader)
                self.line_num += 1
        try:
            attributes = dict(zip(self._fieldnames, next(self._iterator)))
            fancy_row = FancyReader.Row(**attributes)
            self.line_num += 1
            return fancy_row
        except StopIteration:
            self._iterator = None
            raise

