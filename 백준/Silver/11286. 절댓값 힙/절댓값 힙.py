#11286
from sys import stdin
from heapq import heappush,heappop
input = stdin.readline
heap = []
for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap,(abs(x),x))