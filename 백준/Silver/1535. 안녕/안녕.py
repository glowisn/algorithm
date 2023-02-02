#1535
from itertools import combinations

n = int(input())
l = list(map(int,input().split()))
j = list(map(int,input().split()))
table = []
for i in range(n):
    table.append([l[i],j[i]])

maxjoy = 0

for num in range(1,n+1):
    for meet in combinations(table,num):
        hp,joy = 0,0
        for e in meet:
            hp += e[0]
            joy += e[1]
        if hp < 100:
            maxjoy = max(maxjoy,joy)

print(maxjoy)