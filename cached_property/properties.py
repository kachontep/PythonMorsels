class cached_property:
    def __init__(self, func):
        self._getter_func = func
        self._setter_func = None
        self._deleter_func = None
        self._values = dict()

    def setter(self, func):
        self._setter_func = func
        return self

    def deleter(self, func):
        self._deleter_func = func
        return self

    def _cache_key(self, instance):
        return id(instance)

    def __get__(self, instance, owner=None):
        if not instance and owner:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        key = self._cache_key(instance)
        try:
            return self._values[key]
        except KeyError:
            self._values[key] = (self._getter_func)(instance)
            return self._values[key]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
        # Hook for setter
        if self._setter_func:
            (self._setter_func)(instance, value)

    def __delete__(self, instance):
        try:
            del self._values[self._cache_key(instance)]
            del instance.__dict__[self._name]
        except KeyError:
            pass
        # Hook for deleter
        if self._deleter_func:
            (self._deleter_func)(instance)

    def __set_name__(self, owner, name):
        self._name = name
