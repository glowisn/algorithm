#11660
from sys import stdin
input = stdin.readline

def solve(x1,y1,x2,y2):
    global sum_table
    return sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]

n,m = map(int,input().split())
table = [[] for _ in range(n+1)]
table[0] = [0] * (n+1)
sum_table = [[] for _ in range(n+1)]
sum_table[0] = [0] * (n+1)
for i in range(1,n+1):
    table[i] = [0] + list(map(int,input().split()))
    sum_table[i] = [0] * (n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_table[i][j] = sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1] + table[i][j]

for i in range(m):
    # x1,y1,x2,y2 
    print(solve(*list(map(int,input().split()))))