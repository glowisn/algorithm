#1149
n = int(input())
cost = list(map(int,input().split()))

for i in range(n-1):
    r,g,b = map(int,input().split())
    cost = [r+min(cost[1],cost[2]),g+min(cost[0],cost[2]),b+min(cost[0],cost[1])]

print(min(cost))