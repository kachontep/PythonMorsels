SENTINEL = {}


class Unpacker:
    def __init__(self, attrs=SENTINEL):
        super().__setattr__("_attrs", attrs.copy())

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return tuple([self._attrs[k] for k in key])
        else:
            return self._attrs[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            keys, values = key, list(value)
            if len(values) != len(keys):
                raise ValueError("Mismatch lenght for key and value in item assignment")
            for k, v in zip(key, values):
                self._attrs[k] = v
        else:
            self._attrs[key] = value

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def __iter__(self):
        yield from self._attrs.values()

    def __repr__(self):
        return "Unpacker({})".format(
            ", ".join([f"{k}={repr(v)}" for k, v in self._attrs.items()])
        )
