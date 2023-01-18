#14501
n = int(input())
css = []
maxx = []
for _ in range(n):
    css.append(list(map(int,input().split())))
    maxx.append(0)
maxx.append(0)

for i in range(n-1,-1,-1):
    if css[i][0] + i > n :
        maxx[i] = maxx[i+1]
    else:
        maxx[i] = max(maxx[i+1] , maxx[i+css[i][0]] + css[i][1])

print(max(maxx))