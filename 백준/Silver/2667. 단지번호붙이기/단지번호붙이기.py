#2667
from sys import stdin
input = stdin.readline
from collections import deque


def solve(graph,N):
    nodes ,houses = [],[]
    queue = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(N):
        for j in range(N):
            nodes.append((j,i))
    
    for node in nodes:
        if graph[node[1]][node[0]] == 1:
            graph[node[1]][node[0]] = 0
            queue.append((node[0],node[1]))
        
        cnt = 0
        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx,ny))
            cnt += 1
        
        if cnt != 0:
            houses.append(cnt)
    houses.sort()
    print(len(houses))
    print(*houses,sep='\n')


    return


N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

solve(graph,N)