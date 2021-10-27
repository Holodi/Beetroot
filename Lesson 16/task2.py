def in_range(start, end, step=1):
    if start < end:
        while start < end:
            start += abs(step)
            yield start - abs(step)
    else:
        while start > end:
            start -= abs(step)
            yield start + abs(step)


r = in_range(1, -10, -2)
for i in r:
    print(i)
print("*" * 80)
for i in range(1, -10, -2):  #
    print(i)
