#1783
n, m = map(int,input().split())

if n == 1:
    ans = 1
elif n == 2:
    ans = min(4,(m + 1) // 2)
else:
    if m > 6:
        ans = m - 2
    else:
        ans = min(4,m)
print(ans)