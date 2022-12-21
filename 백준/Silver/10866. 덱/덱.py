#10866
from sys import stdin
input = stdin.readline 

dec = []

def myDeque(inputstr):
    ina = list(map(str,inputstr.split()))
    if ina[0] == "push_front":
        dec.insert(0,int(ina[1]))
    elif ina[0] == "push_back":
        dec.append(int(ina[1]))
    elif ina[0] == "pop_front":
        if len(dec) == 0:
            print(-1)
        else:
            print(dec.pop(0))
    elif ina[0] == "pop_back":
        if len(dec) == 0:
            print(-1)
        else:
            print(dec.pop())
    elif ina[0] == "size":
        print(len(dec))
    elif ina[0] == "empty":
        if len(dec) == 0:
            print(1)
        else:
            print(0)
    elif ina[0] == "front":
        if len(dec) == 0:
            print(-1)
        else:
            print(dec[0])
    elif ina[0] == "back":
        if len(dec) == 0:
            print(-1)
        else:
            print(dec[-1])

N = int(input())

for _ in range(N):
    myDeque(str(input()))