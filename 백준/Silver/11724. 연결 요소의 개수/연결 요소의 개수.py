#11724
from sys import stdin
input = stdin.readline
from collections import deque

def solve(graph,n):
    nodes = [i for i in range(1,n+1)]
    visited = [False for _ in range(n+1)]
    queue = deque()
    cnt = 0

    for node in nodes:
        if not visited[node]:
            queue.append(node)
            visited[node] = True
            cnt += 1
            
        while queue:
            t = queue.popleft()
            for el in graph[t]:
                if not visited[el]:
                    queue.append(el)
                    visited[el] = True

    return cnt
        
    


n,m = map(int,input().rsplit())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().rsplit())
    graph[u].append(v)
    graph[v].append(u)

print(solve(graph,n))
