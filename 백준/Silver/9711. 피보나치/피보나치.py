dp = [0, 1, 1]
for i in range(3, 10001):
    dp.append(dp[i-1]+dp[i-2])
t = int(input())
for i in range(1, t+1):
    p, q = map(int, input().split())
    print("Case #" + str(i) + ":", dp[p]%q)