#1021
from collections import deque
N,M = map(int,input().split())
arr = deque([i for i in range(1,N+1)])
want = list(map(int,input().split()))

def min_rotate(arr:deque,size,num):
    ind = arr.index(num)
    rotation = 0
    if ind <= size - ind: # clockwise rotation : -1
        rotation = ind
        arr.rotate(-rotation)
    else: # counterclockwise rotation : 1
        rotation = size - ind
        arr.rotate(rotation)
    return rotation

rotates = 0

for i in range(M):
    rotates += min_rotate(arr,N,want[i])
    arr.popleft()
    N -= 1

print(rotates)