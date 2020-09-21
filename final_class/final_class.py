def init_subclass(cls, **kwargs) -> None:
    raise TypeError(f"type '{cls.__name__}' is not an accpetable base type")


class Unsubclassable:
    __init_subclass__ = init_subclass


def final_class(clazz):
    class FinalClazz(clazz):
        __init_subclass__ = init_subclass

    return FinalClazz


class UnsubclassableType(type):
    def __new__(cls, name, bases, dct):
        t = super().__new__(cls, name, bases, dct)
        t.__init_subclass__ = init_subclass
        return t
