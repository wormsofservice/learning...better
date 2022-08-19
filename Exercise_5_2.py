#determine the largest number in a set using a for loop
from random import random

set = [random(), random(), random(), random(), random(), random()]

print(set)

largest = 0
smallest = 1
for i in set:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i


print(largest)
print(max(set))

print(smallest)
print(min(set))

total = 0

for i in set:
    total += i

print(total)
#print(average(set))
