#17212
n = int(input())
dp = [None for _ in range(n+1)]
dp[:8] = [0,1,1,2,2,1,2,1]

if n % 7 == 3:
    cnt = 2
    for i in range(10,n+1,7):
        dp[i] = cnt
        cnt += 1
else:
    for i in range(8,n+1):
        dp[i] = dp[i-7] + 1

print(dp[n])