#1927
from sys import stdin
input = stdin.readline
from heapq import heappush,heappop

heap = []
for _ in range(int(input())):
    t = int(input())
    if t == 0:
        try:
            print(heappop(heap))
        except:
            print(0)
    else:
        heappush(heap,t)