#2309
from itertools import combinations
keys = []
sumK = 0
for _ in range(9):
    keys.append(int(input()))

sumK = sum(keys)
sumK -= 100
c = []

for i in list(combinations(keys,2)):
    if(i[0] + i[1] == sumK):
        c = i
        break

keys.sort()
for e in keys:
    if(e in c):
        continue
    else:
        print(e)