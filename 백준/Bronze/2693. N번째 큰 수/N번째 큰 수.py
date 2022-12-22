#2693 N번째 큰 수
from sys import stdin
input = stdin.readline 

for _ in range(int(input())):
    A = sorted(list(map(int,input().split())), reverse=True)
    print(A[2])


