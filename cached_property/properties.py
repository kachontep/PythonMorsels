class cached_property:
    def __init__(self, func):
        self._func = func
        self._values = dict()

    def _cache_key(self, instance):
        return id(instance)

    def __get__(self, instance, owner=None):
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        key = self._cache_key(instance)
        try:
            return self._values[key]
        except KeyError:
            self._values[key] = (self._func)(instance)
            return self._values[key]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

    def __delete__(self, instance):
        try:
            del self._values[self._cache_key(instance)]
            del instance.__dict__[self._name]
        except KeyError:
            pass

    def __set_name__(self, owner, name):
        self._name = name
