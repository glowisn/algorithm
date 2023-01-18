#2748
def fib(n):
    global dp
    if dp[n] == None:
        dp[n] = fib(n-2) + fib(n-1)
        return dp[n]
    else:
        return dp[n]
n = int(input())
dp = [None for _ in range(91)]
dp[0] = 0
dp[1] = 1
print(fib(n))