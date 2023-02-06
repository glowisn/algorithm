#10815
import sys
input = sys.stdin.readline
N = int(input())
A = set(map(int,input().rsplit()))
M = int(input())
B = list(map(int,input().rsplit()))
for e in B:
    if e in A:
        print(1,end=' ')
    else:
        print(0,end=' ')