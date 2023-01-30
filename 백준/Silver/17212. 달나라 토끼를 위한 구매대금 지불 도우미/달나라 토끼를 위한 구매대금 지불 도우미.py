#17212
n = int(input())
dp = [None for _ in range(n+1)]
dp[:8] = [0,1,1,2,2,1,2,1]

for i in range(8,n+1):
    dp[i] = dp[i-7] + 1
if n % 7 == 3 and n > 7:
    dp[n] -= 1

print(dp[n])