#2664
from sys import stdin
input = stdin.readline

N = int(input().rstrip())
a,b = map(int,input().rsplit())

m = int(input().rstrip())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = -1

for _ in range(m):
    x,y = map(int,input().rsplit())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start,target,num=0):
    global ans
    visited[start] = 1
    if start==target:
        ans = num

    for node in graph[start]:
        if visited[node] == 0:
            dfs(node,target,num + 1)

    return num

dfs(a,b)
print(ans)