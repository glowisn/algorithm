#14503
from sys import stdin
input = stdin.readline

N,M = map(int,input().rsplit())
r,c,d = map(int,input().rsplit())
room = [list(map(int,input().rsplit())) for _ in range(N)]

def setdir(dir):
    dx,dy = 0,0
    if dir == 0: # north
        dy = -1
    if dir == 1: # east
        dx = 1
    if dir == 2: # south
        dy = 1
    if dir == 3: # west
        dx = -1

    return dx,dy

dx,dy = setdir(d)

def turnCounterClock(d):
    d = (d-1)%4
    dx,dy = setdir(d)

    return d,dx,dy
    

cnt = 0

while True:
    #1
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    #2
    if room[r+1][c] != 0 and room[r-1][c] !=0 and room[r][c+1] !=0 and room[r][c-1] !=0:
        #1
        if room[r-dy][c-dx] != 1:
            r -= dy
            c -= dx
        #2
        else:
            print(cnt)
            break
    #3
    else:
        #1
        d,dx,dy = turnCounterClock(d)
        #2
        if room[r+dy][c+dx] == 0:
            r += dy
            c += dx
        #3
    
# print(*room,sep='\n')
