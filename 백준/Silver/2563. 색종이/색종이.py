#2563
from sys import stdin
input = stdin.readline

paper = []
for i in range(100):
    paper.append([])
    for j in range(100):
        paper[i].append(0)


def color(point:list):
    global paper
    for i in range(point[0],point[0]+10):
        for j in range(point[1],point[1]+10):
            paper[i][j] = 1

n = int(input())

points = [list(map(int,input().split())) for _ in range(n)]

for point in points:
    color(point)

ans = 0

for i in range(100):
    ans += paper[i].count(1)

print(ans)

