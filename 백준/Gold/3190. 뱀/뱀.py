#3190
import sys
input = sys.stdin.readline

from collections import deque
import itertools

import time

def showscreen(board,time):
    print("Time : ",time)
    # print("**" * len(board))
    for e in board[1:]:
        # print("*",end=' ')
        print(*e[1:],sep=' ')
    # print("**" * len(board))

def isdead(board,snake:deque) -> bool:
    #dead by head collison on wall
    if snake[-1][0] == n+1 or snake[-1][0] == 0 or snake[-1][1] == n+1 or snake[-1][1] == 0:
        # print("DEBUG: Dead Here: ",snake[-1])
        return True
    #dead by touching itself
    body = deque(itertools.islice(snake,0,len(snake)-1))
    if snake[-1] in body:
        return True
    #live
    return False

def snakeGo(board:list,snake:deque,currDir:list,dir:str):
    dead = False
    newSnake = [snake[-1][0] + currDir[0],snake[-1][1] + currDir[1]]

    #dead by touching itself
    body = deque(itertools.islice(snake,0,len(snake)-1))
    if newSnake in body:
        dead = True
        # return board,snake,currDir,True
    #dead by toching wall
    if newSnake[0] == n+1 or newSnake[0] == 0 or newSnake[1] == n+1 or newSnake[1] == 0:
        dead = True
        # return board,snake,currDir,True
    
    snake.append(newSnake)

    # is NOT Apple
    if board[newSnake[0]][newSnake[1]] != "A":
        traceSnake = snake.popleft()
        board[traceSnake[0]][traceSnake[1]] = "0"
    board[newSnake[0]][newSnake[1]] = "H"

    if dir == "D": # turn right
        if currDir[0] == 0:
            currDir[0],currDir[1] = currDir[1],currDir[0]
        else:
            currDir[0],currDir[1] = -currDir[1],-currDir[0]
    if dir == "L":
        if currDir[0] == 0:
            currDir[0],currDir[1] = -currDir[1],-currDir[0]
        else:
            currDir[0],currDir[1] = currDir[1],currDir[0]
    
    # print(snake)
    return board,snake,currDir,dead

n = int(input().rstrip())
k = int(input().rstrip())
board = [[0] * (n+2) for _ in range(n+2)]

# #벽 배치
# for i in range(n+2):
#     board[0][i] = "*"
#     board[i][0] = "*"
#     board[i][n+1] = "*"
#     board[n+1][i] = "*"

##사과 배치
for _ in range(k):
    c,r = map(int,input().rsplit())
    board[c][r] = "A"

##방향 전환 정보
dirs = []
l = int(input().rstrip())
for _ in range(l):
    t = list(input().rsplit())
    dirs.append([int(t[0]),t[1]])

##뱀 배치
board[1][1] = "H"


# showscreen(board,0)


snake = deque([[1,1]])
currDir = [0,1] # 0,1:Right // 1,0:Down // 0,-1:Left, // -1,0:Up
dir = "N"
i = 1
dead = False
while True:
    dir = "N"
    if dirs and dirs[0][0] == i:
        # print("Dir change Time!",i,dirs[0])
        dir = dirs.pop(0)[1] #"D":rightR,"L":leftR
    board,snake,currDir,dead = snakeGo(board,snake,currDir,dir)
    #
    # showscreen(board,i)
    # time.sleep(0.5)
    #
    if dead:
        break
    i += 1

print(i)
    
