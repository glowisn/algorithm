#2178
from collections import deque

N,M = map(int,input().split())
site = [list(map(int,list(input()))) for _ in range(N)]
visited = [[0]* M for _ in range(N)]

visited[0][0] = 1

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if site[nx][ny] == 0:
                continue

            if site[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    # print(*visited,sep='\n')
    
    return visited[N-1][M-1]

print(bfs(0,0))