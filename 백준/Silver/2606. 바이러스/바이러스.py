#2606
from collections import deque

def bfs(graph,n):
    visited = [False for _ in range(n+1)]
    queue = deque([1])

    while queue:
        n = queue.popleft()
        if not visited[n]:
            visited[n] = True
            for el in graph[n]:
                if not visited[el]:
                    queue.append(el)
    
    return visited


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph,n).count(True)-1)

