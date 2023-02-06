#1920
from sys import stdin
input = stdin.readline
N = int(input())
A = set(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
for e in B:
    print(1) if e in A else print(0)