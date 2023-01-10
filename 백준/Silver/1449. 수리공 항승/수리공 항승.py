#1449_re
N, L = map(int,input().split())
holes = list(map(int,input().split()))
holes.sort()
tapes = []
tapecnt = 0
for h in holes:
    if h not in tapes:
        tapecnt += 1
        for i in range(L):
            tapes.append(h+i)
print(tapecnt)