#1158
from collections import deque
N, K = map(int, input().split())
dec = deque([i+1 for i in range(N)])
ans = []

for _ in range(N):
    dec.rotate(-(K-1))
    ans.append(str(dec.popleft()))

print("<",", ".join(ans)[:],">", sep='')