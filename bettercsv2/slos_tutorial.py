import timeit

class Foo(object): __slots__ = 'foo',

class Bar(object): pass

slotted = Foo()
not_slotted = Bar()


def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo
    return get_set_delete_fn
