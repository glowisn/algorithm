import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

summ = 0
cnt = 0
sd = {0:1}
for i in arr:
    summ += i
    if summ - k in sd.keys():
        cnt += sd[summ - k]
    if summ in sd.keys():
        sd[summ] += 1
    else:
        sd[summ] = 1

    


print(cnt) 