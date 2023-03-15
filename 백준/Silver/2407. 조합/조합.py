#2407
n,m = map(int,input().rsplit())
## nCm = n*(n-1)*(n-2)...(n-(m-1)) // m*(m-1)*(m-2)...1
if m > n/2:
    m = n - m
ans = 1
tmp = 1
for i in range(m):
    ans *= (n-i)
for i in range(1,m+1):
    tmp *= i

print(ans//tmp)