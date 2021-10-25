#The greatest number

from random import randint
list1 = []
while len(list1) != 10:
    list1.append(randint(1, 10))
list1.sort()
print(list1[-1])
