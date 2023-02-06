#11866
from collections import deque
N,K = map(int,input().split())
q = deque([i for i in range(1,N+1)])
ans = []
while q:
    q.rotate(-K)
    ans.append(q.pop())

print("<",end='')
print(*ans,sep=', ',end='')
print(">")