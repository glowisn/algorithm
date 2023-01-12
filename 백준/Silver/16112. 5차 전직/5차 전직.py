#16112
n , k = map(int,input().split())
exps = list(map(int,input().split()))
exps.sort()

summ = 0

for i in range(k):
    summ += exps[i] * i

for j in range(k,len(exps)):
    summ += exps[j] * k

print(summ)