
def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


s = {1, "string", 4, True}
print(list(with_index(s, 10)))
