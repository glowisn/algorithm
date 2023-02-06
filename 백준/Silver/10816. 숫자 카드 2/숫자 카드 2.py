#10816
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

for b in B:
    try:
        print(dic[b],end=' ')
    except:
        print(0,end=' ')

    
