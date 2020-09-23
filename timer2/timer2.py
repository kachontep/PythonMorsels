from re import L
import time


def Timer(name=None):
    return TimerClz.create_timer(name) if name else TimerClz()


class TimerClz:
    _registry = {}

    @classmethod
    def create_timer(cls, name):
        try:
            return cls._registry[name]
        except KeyError:
            new_timer = cls(name)
            cls._registry[name] = new_timer
            return new_timer

    def __init__(self, name=None):
        self._name = name or self.__class__.__name__.title()
        self.elapsed = None
        self._start = None
        self._children = []
        self._children_registry = {}
        self._default_child_num = 0
        self.runs = []

    def _default_child_name(self):
        child_name = "{}_{}".format(self._name, self._default_child_num)
        self._default_child_num += 1
        return child_name

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self._start
        self.runs.append(self.elapsed)
        self._start = None

    def split(self, name=None):
        if self._start is None:
            raise RuntimeError("Cannot split because parent timer is not running")
        try:
            return self._children_registry[name]
        except KeyError:
            return self._create_child(name or self._default_child_name())

    def _create_child(self, name):
        child = TimerClz(name)
        self._children.append(child)
        self._children_registry[child._name] = child
        return child

    def __getitem__(self, key):
        if isinstance(key, str):
            try:
                return self._children_registry[key]
            except KeyError:
                raise IndexError("Timernamed '{}' not found".format(key))
        else:
            return self._children[key]

