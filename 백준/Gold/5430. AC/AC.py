#5430
from sys import stdin
input = stdin.readline

from collections import deque

def printThat(arr):
    if arr == "Error":
        print("error")
        return
    print("[",end='')
    print(*arr,sep=',',end="]\n")

def getArr(ipt:str):
    if ipt == "[]":
        return deque([])
    x = []
    t = ipt[1:-1]
    tmp = ""
    for al in t:
        if al == ",":
            x.append(int(tmp))
            tmp = ""
        else:
            tmp += al
    if tmp:
        x.append(int(tmp))

    return deque(x)

def instruct(arr:deque,p:str):
    rev = 0
    for ins in p:
        if ins == "R":
            rev += 1
        if ins == "D":
            if arr:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                return "Error"
    if rev % 2 == 1:
        arr.reverse()
    
    return arr
                

for _ in range(int(input().rstrip())):
    p = input().rstrip()
    n = int(input().rstrip())
    x = getArr(input().rstrip())
    arr = instruct(x,p)
    printThat(arr)
    