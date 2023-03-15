#7569
from sys import stdin
input = stdin.readline
from collections import deque

M,N,H = map(int,input().rsplit())

graph = []

for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int,input().rsplit())))
    graph.append(tmp)

def bfs():
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
    dx = [0,0,-1,1,0,0]
    dy = [0,0,0,0,-1,1]
    dz = [-1,1,0,0,0,0]

    while que:
        x,y,z = que.popleft()

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z

            if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                continue

            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                que.append([nx,ny,nz])

    return

que = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                que.append([x,y,z])

bfs()

#answer

maxer = -1
for itt in graph:
    for it in itt:
        for i in it:
            maxer = max(i,maxer)
            if i == 0:
                print(-1)
                quit()


print(maxer-1)