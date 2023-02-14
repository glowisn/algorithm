#1012
from sys import stdin
input = stdin.readline

from collections import deque

def solve(nodes,graph,M,N):
    cnt = 0
    queue = deque()

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    for node in nodes:
        if graph[node[1]][node[0]] == 1:
            queue.append(node)
            cnt += 1
        
        while queue:
            x,y = queue.popleft()
            graph[y][x] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue

                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx,ny))


    return cnt

ans = []
for _ in range(int(input())):
    M,N,K = map(int,input().rsplit())
    nodes = []
    graph = [[0]* M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().rsplit())
        nodes.append((x,y))
        graph[y][x] = 1
    ans.append(solve(nodes,graph,M,N))

print(*ans,sep='\n')