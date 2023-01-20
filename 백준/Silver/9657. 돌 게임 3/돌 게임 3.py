#9657
n = int(input())
dp = [0 for _ in range(n+1)]
dp[1:5] = [1,-1,1,1]
for i in range(5,n+1):
    dp[i] = max(-dp[i-1],-dp[i-3],-dp[i-4])
print("SK") if dp[n] == 1 else print("CY")