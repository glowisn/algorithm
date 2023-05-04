#10810
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
basket = [0] * (n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    basket[i:j+1] = [k] * (j+1-i)

print(*basket[1:])

