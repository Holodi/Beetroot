
class Iterable:

    def __init__(self, iterable):
        self._iterable = iterable
        self._index = len(iterable)
        self._i = -1

    # def __getitem__(self, item):
    #     self._i += 1
    #     return self._iterable[self._i]

    def __iter__(self):
        return (self)

    def __next__(self):
        self._i += 1
        if self._i == self._index:
            raise StopIteration
        return self._iterable[self._i]


iter = Iterable("asdlaksdlajhs")
for i in iter:
    print(i)
