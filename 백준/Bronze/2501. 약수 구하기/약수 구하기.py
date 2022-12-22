#2501

N, K = map(int,input().split())

divs = []

for i in range(1,N+1):
    if N % (i) == 0:
        divs.append(i)

if len(divs) < K:
    print(0)
else:
    print(divs[K-1])
