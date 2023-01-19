#1904
n = int(input())
dp = [0 for _ in range(n+1)]

dp[0:2] = [1,1,2]

for i in range(3,n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])