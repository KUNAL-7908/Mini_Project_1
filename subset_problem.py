# Subset Selection Problem Part 1
import random as r
MySet = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
size = 5
result = set()
for i in range(1000):
    element = r.sample(MySet,size)
    element.sort()
    # summing up
    if sum(element) == 0:
        result.add(tuple(element))

for j in result:
    print(j)

print(len(result))