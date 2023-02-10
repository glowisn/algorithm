#13335
from sys import stdin
input = stdin.readline
from collections import deque


from time import sleep

def runnigB(bridge:deque):
    for e in bridge:
        if e != 0:
            return True
    return False

n,w,L = map(int,input().rsplit())
a = deque(list(map(int,input().rsplit())))
bridge = deque([0 for _ in range(w)])

time = 0

while a or runnigB(bridge):
    #out
    bridge.rotate(-1)
    L += bridge[-1]
    bridge[-1] = 0
    #in
    if a and a[0] <= L:
        t = a.popleft()
        L -= t
        bridge[-1] = t

    # print("time:",time," a:",a," bridge:",bridge," weight:",L)
    time += 1



print(time)
