#11726
def hash(n:int):
    global dp
    if dp[n] == None:
        return False
    else:
        return dp[n]

def recursion(n:int):
    if hash(n):
        return dp[n]
    else:
        if n % 2 == 0: # even
            dp[n] = (recursion(n//2) ** 2) + (recursion(n//2 - 1) ** 2)
            return dp[n]
        else:
            dp[n] = (recursion(n//2 + 1) * recursion(n//2)) + (recursion(n//2) * recursion(n//2 - 1))
            return dp[n]

n = int(input())

dp = [None for _ in range(n+3)]

dp[0],dp[1],dp[2]= 1,1,2

print(recursion(n) % 10007)