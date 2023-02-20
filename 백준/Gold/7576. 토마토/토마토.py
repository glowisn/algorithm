#7576
from sys import stdin
input = stdin.readline

from collections import deque

m,n = map(int,input().rsplit())
box = [list(map(int,input().rsplit())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

queue = deque()

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            queue.append((x,y))

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            queue.append((nx,ny))

maxer = -1

for y in range(n):
    for x in range(m):
        if box[y][x] == 0:
            print(-1)
            quit()
        maxer = max(maxer,box[y][x])
        
print(maxer-1)