#2164
from collections import deque

deq = deque([i+1 for i in range(int(input()))])

while(len(deq) != 1):
    deq.popleft()
    deq.rotate(-1)

print(deq[0])