#11279
import heapq
from sys import stdin
input = stdin.readline

heap = []

def heaper(i):
    if i == 0:
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, i)
        
for _ in range(int(input())):
    heaper((int(input()) * -1))