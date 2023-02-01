#11052
n = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(len(p))]
#dp[i] = dp[i-k] + p[i]

for i in range(1,len(p)):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])


print(dp[-1])