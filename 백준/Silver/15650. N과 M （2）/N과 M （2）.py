#15650
from itertools import combinations

N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for e in list(combinations(arr,M)):
    print(*e)
