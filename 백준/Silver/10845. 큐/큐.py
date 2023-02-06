#10845
from sys import stdin
input = stdin.readline
q = []
for _ in range(int(input())):
    ins = list(input().split())
    if ins[0] == "push":
        q.append(ins[1])
    if ins[0] == "pop":
        try:
            print(q.pop(0))
        except:
            print(-1)
    if ins[0] == "size":
        print(len(q))
    if ins[0] == "empty":
        print(0) if q else print(1)
    if ins[0] == "front":
        try:
            print(q[0])
        except:
            print(-1)
    if ins[0] == "back":
        try:
            print(q[-1])
        except:
            print(-1)
