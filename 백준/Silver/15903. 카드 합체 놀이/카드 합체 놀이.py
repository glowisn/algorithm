#15903
n,m = map(int,input().split())
a = list(map(int,input().split()))

for i in range(m):
    a.sort()
    t = a[0]+a[1]
    a[0],a[1] = t,t

print(sum(a))