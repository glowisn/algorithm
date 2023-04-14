#14891
from collections import deque
#from 12'o clockwise, 0 for N 1 for S
gears = []
for _ in range(4):
    gears.append(deque(map(int,input())))


def checkR(num):
    if gears[num][2] == gears[num+1][6]:
        return False
    else:
        return True

def checkL(num):
    if gears[num-1][2] == gears[num][6]:
        return False
    else:
        return True


def checkgreen(gea)->list:
    #1이면 극이 달라서 같이 회전, 0이면 극이 같아서 회전 안함
    toRotate = [0,0,0,0]

    if gea == 0:
        toRotate[0] = 1
        if checkR(0):
            toRotate[1] = -1
            if checkR(1):
                toRotate[2] = 1
                if checkR(2):
                    toRotate[3] = -1

    if gea == 1:
        toRotate[1] = 1
        if checkL(1):
            toRotate[0] = -1
        if checkR(1):
            toRotate[2] = -1
            if checkR(2):
                toRotate[3] = 1

    if gea == 2:
        toRotate[2] = 1
        if checkL(2):
            toRotate[1] = -1
            if checkL(1):
                toRotate[0] = 1
        if checkR(2):
            toRotate[3] = -1

    if gea == 3:
        toRotate[3] = 1
        if checkL(3):
            toRotate[2] = -1
            if checkL(2):
                toRotate[1] = 1
                if checkL(1):
                    toRotate[0] = -1


    # print(toRotate)
    return toRotate


def rotate(gear:int,dir:int):
    global gears
    toRotate = checkgreen(gear)
    
    for i in range(4):
        gears[i].rotate(toRotate[i]*dir)

    return gears

def scoring(gears):
    score = 0
    # 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    if gears[0][0] == 1:
        score += 1
    # 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    if gears[1][0] == 1:
        score += 2
    # 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    if gears[2][0] == 1:
        score += 4
    # 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
    if gears[3][0] == 1:
        score += 8


    return score

for _ in range(int(input())):
    gear, dir = map(int,input().rsplit())
    rotate(gear-1,dir)

# for g in gears:
#     print(*g,sep='')

print(scoring(gears))