#1946
from sys import stdin
input = stdin.readline

def employment(scores:list,N):
    employ = 1
    scores.sort(key=lambda x:x[0])
    maxx = scores[0][1]
    for i in range(1,N):
        if scores[i][1] < maxx:
            maxx = scores[i][1]
            employ += 1

    print(employ)


T = int(input())

for _ in range(T):
    N = int(input())
    scores = []
    for i in range(N):
        scores.append(list(map(int,input().split())))
    employment(scores,N)