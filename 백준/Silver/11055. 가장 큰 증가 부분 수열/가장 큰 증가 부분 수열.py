#11055

n = int(input())
a = [0] + list(map(int,input().split()))
dp = a[:]
for i in range(2,n+1):
    for j in range(1,i):
        if a[j] < a[i] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]
    
print(max(dp))
