class WindowSlider:
    def __init__(self, iterable, size):
        self._iterable = iterable
        self._size = size
        self._len = 0
        self._lastitems = []

    def capture(self, fillvalue=None):
        items = []
        captured = False
        for e in self._iterable:
            items.append(e)
            self._lastitems = items
            if len(items) == self._size:
                captured = True
            if not captured:
                continue
            yield tuple(items)
            self._len += 1
            items = items[1:]
        if self._len == 0 and len(self._lastitems) < self._size:
            yield (
                tuple(self._lastitems)
                + ((fillvalue,) * (self._size - len(self._lastitems)))
            )


def window(iterable, size, **kwargs):
    fillvalue = kwargs.get("fillvalue", None)
    slider = WindowSlider(iterable, size)
    return slider.capture(fillvalue)
