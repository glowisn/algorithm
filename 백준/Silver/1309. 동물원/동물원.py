#1309
n = int(input())
dp = [0 for _ in range(n+1)]
cp = [0 for _ in range(n+1)]

dp[1],cp[1] = 3,2

for i in range(2,n+1):
    dp[i] = (dp[i-1] + cp[i-1] * 2) % 9901
    cp[i] = (dp[i-1] + cp[i-1]) % 9901

print(dp[-1] % 9901)