#Exclusive common numbers

from random import randint

list1 = []
while len(list1) != 10:
    list1.append(randint(1, 20))
print(list1)
list2 = []
while len(list2) != 10:
    list2.append(randint(1, 20))
print(list2)

list3 = set(list1+list2)

print(list3)