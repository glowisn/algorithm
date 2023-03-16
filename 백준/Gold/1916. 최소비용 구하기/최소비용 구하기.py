#1916
from sys import stdin
input = stdin.readline
import heapq

INF = int(1e9)

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[]for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a,b,d = map(int,input().rsplit())
    graph[a].append((b,d))

start,target = map(int,input().rsplit())

def dijkstra(num):
    q = []
    heapq.heappush(q,(num,0))
    distance[num] = 0

    while q:
        x,d = heapq.heappop(q)
        if distance[x] < d:
            continue
        for dx,dd in graph[x]:
            nd = d + dd
            if distance[dx] > nd:
                distance[dx] = nd
                heapq.heappush(q,(dx,nd))

dijkstra(start)

print(distance[target])
# print(distance)