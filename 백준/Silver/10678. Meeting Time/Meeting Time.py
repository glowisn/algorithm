#10678
bill = [[],[]]

def travel(paths,start,N,who,time = 0):
    if start == N:
        # Goal
        global bill
        bill[who].append(time)
        return
    
    for des, cost in paths[start].items():
        travel(paths,des,N,who,time+cost[who])

N, M = map(int,input().split())
paths = []
for _ in range(N):
    paths.append({})

for i in range(M):
    ta,tb,tc,td = map(int,input().split())
    paths[ta][tb] = [tc,td]

for j in range(2):
    travel(paths,1,N,j)
    bill[j].sort()

for cost in bill[0]:
    if cost in bill[1]:
        print(cost)
        quit()

print("IMPOSSIBLE")
