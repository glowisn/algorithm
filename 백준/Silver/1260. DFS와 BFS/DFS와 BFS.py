#1260
from collections import deque

def dfs(graph,root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                graph[n].sort(reverse=True)
                for el in graph[n]:
                    if el not in visited:
                        stack.append(el)
    
    return visited

def bfs(graph,root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                graph[n].sort()
                for el in graph[n]:
                    if el not in visited:
                        queue.append(el)
    
    return visited


n,m,v = map(int,input().split())
graph = {}
for _ in range(m):
    sn,en = map(int,input().split())
    if sn in graph:
        graph[sn] += [en]
    else:
        graph[sn] = [en]
    if en in graph:
        graph[en] += [sn]
    else:
        graph[en] = [sn]

for key in graph:
    graph[key].sort()

# print(graph)

print(*dfs(graph,v))
print(*bfs(graph,v))
