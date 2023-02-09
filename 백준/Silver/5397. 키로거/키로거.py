#5397
from sys import stdin
input = stdin.readline
for _ in range(int(input().rstrip())):
    t = input().rstrip()
    a,b = [],[]
    for e in t:
        if e == "<":
            if a:
                b.append(a.pop())
        elif e == ">":
            if b:
                a.append(b.pop())
        elif e == "-":
            if a:
                a.pop()
        else:
            a.append(e)
    print(*a,*b[::-1],sep='')