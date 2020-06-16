def alias(name: str, write: bool = False):
    class Alias:
        def __init__(self, name: str, write: bool = False):
            self.name = name
            self.write = write

        def __get__(self, instance, owner):
            try:
                return getattr(instance, self.name)
            except AttributeError:
                return getattr(owner, self.name)

        def __set__(self, instance, value):
            if not self.write:
                raise AttributeError("can't set attribute")
            setattr(instance, self.name, value)

    return Alias(name, write)


if __name__ == '__main__':
    class DataRecord:
        title = alias('serial', write=True)

        def __init__(self, serial):
            self.serial = serial

    record = DataRecord('148X')
    record.title = '149S'
    print(record.serial)
