#11725
from sys import stdin
input = stdin.readline
from collections import deque

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().rsplit())
    graph[u].append(v)
    graph[v].append(u)

def bfs(n):
    visited = [0 for _ in range(n+1)]
    que = deque([1])
    visited[1] = 1

    while que:
        n = que.popleft()
        for num in graph[n]:
            if visited[num] == 0:
                que.append(num)
                visited[num] = 1
                parent[num] = n


bfs(n)

print(*parent[2:],sep='\n')