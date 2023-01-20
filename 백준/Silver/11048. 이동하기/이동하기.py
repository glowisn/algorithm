#11048
n,m = map(int,input().split())
field,dp = [],[]
for _ in range(n):
    field.append(list(map(int,input().split())))
    dp.append([0 for _ in range(m)])

dp[0][0] = field[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + field[0][i]
for j in range(1,n):
    dp[j][0] = dp[j-1][0] + field[j][0]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + field[i][j]

# print(*dp,sep='\n')
print(dp[n-1][m-1])