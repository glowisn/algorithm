#2468
from sys import stdin
input = stdin.readline

from collections import deque

def solve(vill,n,h):
    visited,nodes = set(),[]
    queue = deque()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if vill[y][x] > h:
                nodes.append((x,y))
    
    for node in nodes:
        if node not in visited:
            visited.add(node)
            queue.append(node)
            cnt += 1
        
        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                
                if (nx,ny) not in visited and vill[ny][nx] > h:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
    return cnt

n = int(input().rstrip())
vill = [list(map(int,input().rsplit())) for _ in range(n)]
max_h,max_i = 0,0
for vil in vill:
    max_h = max(max(vil),max_h)
for i in range(0,max_h):
    max_i = max(max_i,solve(vill,n,i))

print(max_i)