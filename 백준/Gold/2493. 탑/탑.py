#2493
from sys import stdin
input = stdin.readline

N = int(input().rstrip())
a = [0] + list(map(int,input().rsplit()))

stack = []
ans = []
for i in range(1,N+1):
    rev = 0
    while stack:
        if stack[-1][1] > a[i]:
            rev = stack[-1][0]
            break
        else:
            stack.pop()
    ans.append(rev)
    stack.append([i,a[i]])

print(*ans)