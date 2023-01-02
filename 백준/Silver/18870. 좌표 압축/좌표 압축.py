#18870
from sys import stdin
input = stdin.readline

input()

Xs = list(map(int,input().split()))
Xssrt = sorted(list(set(sorted(Xs))))

dict = {}
for i in range(len(Xssrt)):
    dict[Xssrt[i]] = i

for X in Xs:
    print(dict[X],end=' ')
