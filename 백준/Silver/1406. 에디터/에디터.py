#1406
from sys import stdin
input = stdin.readline
a = list(input().rstrip())
b = []
for _ in range(int(input())):
    t = list(input().rsplit())
    if t[0] == 'L':
        if a:
            b.append(a.pop())
    if t[0] == 'D':
        if b:
            a.append(b.pop())
    if t[0] == 'B':
        if a:
            a.pop()
    if t[0] == 'P':
        a.append(t[1])

b.reverse()
print(*a,*b,sep='')