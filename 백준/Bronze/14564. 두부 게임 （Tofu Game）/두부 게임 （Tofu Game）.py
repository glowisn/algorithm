#14564
from sys import stdin
input = stdin.readline

N,M,A = map(int,input().rsplit())

aa = []
i = M//2 + 1

while True:
    b = int(input())
    if b == i:
        aa.append(0)
        break
    b -= i
    A += b
    if A > N:
        A -= N
    if A <= 0:
        A += N
    aa.append(A)
    
print(*aa,sep='\n')