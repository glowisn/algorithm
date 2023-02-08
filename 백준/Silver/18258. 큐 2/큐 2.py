#18258
from sys import stdin
input = stdin.readline
from collections import deque
que = deque([])
for _ in range(int(input().rstrip())):
    t = list(input().rsplit())
    if t[0] == "push":
        que.append(t[1])
    elif t[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif t[0] == "size":
        print(len(que))
    elif t[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif t[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif t[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)