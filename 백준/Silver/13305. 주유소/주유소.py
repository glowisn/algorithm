#13305

N = int(input())
paths = list(map(int,input().split()))
costs = list(map(int,input().split()))

currcost = costs[0]
summ = 0
for i in range(len(paths)):
    if currcost > costs[i]:
        currcost = costs[i]
    summ += currcost * paths[i]

print(summ)