#14425
from sys import stdin
input = stdin.readline

N,M = map(int,input().rsplit())
S = tuple([input().rstrip() for _ in range(N)])

ans = 0
for _ in range(M):
    t = input().rstrip()
    if t in S:
        ans += 1
    
print(ans)