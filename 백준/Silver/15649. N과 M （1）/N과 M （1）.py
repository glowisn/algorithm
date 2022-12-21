#15649
from itertools import permutations

N, M = map(int,input().split())

arr = [i+1 for i in range(N)]

for e in list(permutations(arr,M)):
    print(*e)