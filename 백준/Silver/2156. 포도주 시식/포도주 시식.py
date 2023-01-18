#2156
n = int(input())
wine = []
maxx = []
for _ in range(n):
    wine.append(int(input()))
    maxx.append(0)
if n == 1 or n == 2:
    print(sum(wine))
    quit()
maxx[0] = wine[0]
maxx[1] = wine[0] + wine[1]
maxx[2] = max(wine[0], wine[1]) + wine[2]
for i in range(3,n):
    maxx[i] = max(maxx[i-2],max(maxx[i-4],maxx[i-3]) + wine[i-1]) + wine[i]

print(max(maxx))