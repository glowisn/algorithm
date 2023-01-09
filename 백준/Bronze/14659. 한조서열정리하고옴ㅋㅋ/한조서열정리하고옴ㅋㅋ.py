#14659

N = int(input())
hills = list(map(int,input().split()))

ma,eat,curr = 0,0,0
for i in range(N):
    if curr < hills[i]:
        curr = hills[i]
        if ma < eat:
            ma = eat
        eat = 0
    else:
        eat += 1

if ma < eat:
    ma = eat

print(ma)