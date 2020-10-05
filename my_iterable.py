class MyIterable:

    def __init__(self, start, stop):
        if not stop > start:
            raise ValueError('Start has to be < than stop')
        self.start = start
        self.stop = stop
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        raise StopIteration


it = MyIterable(stop=3, start=1)
for i in list(it):
    print(i)
