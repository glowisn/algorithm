#1449

N, L = map(int,input().split())

holes = list(map(int,input().split()))

tapes = []
tapecnt = 0
for d in range(1,1001):
    if d in holes and d not in tapes:
        tapecnt += 1
        for i in range(L):
            tapes.append(d+i)

print(tapecnt)