#11403
from sys import stdin
input = stdin.readline

n = int(input().rstrip())
graph = [list(map(int,input().rsplit())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


for i in range(n):
    print(*graph[i])