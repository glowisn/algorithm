#10678
bill = [[],[]]

def travel(start,who,time = 0):
    global paths, N
    if start == N:
        # Goal
        global bill
        bill[who].append(time)
        return
    
    for des, cost in paths[start].items():
        travel(des,who,time+cost[who])

N, M = map(int,input().split())
paths = []
for _ in range(N):
    paths.append({})

for i in range(M):
    ta,tb,tc,td = map(int,input().split())
    paths[ta][tb] = [tc,td]

for j in range(2):
    travel(1,j)
    bill[j].sort()

for cost in bill[0]:
    if cost in bill[1]:
        print(cost)
        quit()

print("IMPOSSIBLE")
