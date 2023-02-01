#11057
n = int(input()) + 1
dp = []
for _ in range(10):
    dp.append([1 for _ in range(n)])

for i in range(1,10):
    for j in range(1,n):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 10007

print(dp[-1][-1])