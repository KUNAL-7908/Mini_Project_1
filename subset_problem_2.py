# Subset problem 2
import random as r

Myset = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
lower = 3
upper = 6
result = set()

for i in range(1000):
    size = r.randint(lower,upper)
    element = r.sample(Myset, size)
    element.sort()
    #summing up
    if sum(element) == 0:
        result.add(tuple(element))

for j in result:
    print(j)
print("Total number of sets are",len(result))