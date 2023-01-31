#11060
import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int,input().split()))
dp = [1001 for _ in range(n+1)]
dp[0:2] = 0,0

for i in range(1,n+1):
    for j in range(1,a[i]+1):
        if i+j <= n:
            dp[i+j] = min(dp[i]+1,dp[i+j])

print(dp[-1]) if dp[-1] != 1001 else print(-1)