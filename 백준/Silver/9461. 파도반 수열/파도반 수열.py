#9461
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [None for _ in range(n+1)]
    dp[0:4] = [0,1,1,1]
    for i in range(4,n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])
