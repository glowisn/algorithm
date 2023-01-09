#1931
from sys import stdin
input = stdin.readline

N = int(input())

meets = [list(map(int,input().split())) for _ in range(N)]

meets.sort(key= lambda x : (x[1], x[0]))

endt = -1
cnt = 0
for e in meets:
    if e[0] >= endt:
        cnt += 1
        endt = e[1]

print(cnt)