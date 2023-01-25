#17175
def fib_num(n:int) -> int:
    dp = [1,1]
    for i in range(2,n+1):
        dp.append((dp[i-2]+dp[i-1] + 1) % 1000000007)
    return dp[n]

print(fib_num(int(input())))