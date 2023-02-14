#4963
from sys import stdin
input = stdin.readline

from collections import deque

def bfs(graph,w,h):
    nodes = []
    visited = []
    queue = deque()
    cnt = 0

    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]


    #graph[h][w] -> graph[i][j]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                nodes.append((j,i))
    
    for node in nodes:
        if node not in visited:
            queue.append(node)
            cnt += 1
        
        while queue:
            x,y = queue.popleft()
            visited.append((x,y))

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx > -1 and nx < w and ny > -1 and ny < h and graph[ny][nx] == 1:
                    if (nx,ny) not in visited:
                        visited.append((nx,ny))
                        queue.append((nx,ny))

    return cnt

while True:
    w,h = map(int,input().rsplit())
    if w == 0 and h == 0:
        break
    graph = [list(map(int,input().rsplit())) for _ in range(h)]

    print(bfs(graph,w,h))
    
