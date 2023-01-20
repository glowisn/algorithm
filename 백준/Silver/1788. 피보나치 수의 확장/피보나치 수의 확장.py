#1788
magic_number = 1000000000
flag = 1
n = int(input())
if n == 0:
    print(0,0,sep='\n')
else:
    dp = [0 for _ in range(abs(n)+1)]
    dp[0:2] = [0,1]
    if n < 0:
        n = -n
        if n % 2 == 0:
            flag = -1
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % magic_number
    print(flag,dp[n] % magic_number,sep='\n')