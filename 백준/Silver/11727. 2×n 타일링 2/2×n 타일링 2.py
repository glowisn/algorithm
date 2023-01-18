#11727

n = int(input())
dp = [None for _ in range(n+1)]
dp[0:3] = [1,1,3]
for i in range(3,n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]
print(dp[n] % 10007)

