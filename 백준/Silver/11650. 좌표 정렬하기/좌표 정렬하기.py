#11650
from sys import stdin
input = stdin.readline 

dots = []
for _ in range(int(input())):
    dots.append(list(map(int, input().split())))

dots.sort(key = lambda x : (x[0], x[1]))

for i in dots:
    print(*i)
