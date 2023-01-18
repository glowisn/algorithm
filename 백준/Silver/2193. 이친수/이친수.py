#2193
def fib(n:int):
    global dp
    if dp[n] != None:
        return dp[n]
    else:
        dp[n] = fib(n-1) + fib(n-2)
        return dp[n]

n = int(input())
dp = [None for _ in range(n+1)]
dp[0:2] = [1,1]
print(fib(n-1))
