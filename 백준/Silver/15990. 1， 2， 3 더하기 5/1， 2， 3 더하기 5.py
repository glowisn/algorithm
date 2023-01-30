#15990
divider = 1000000009
def solvemax(n:int)->int:
    global dp
    for i in range(4,n+1):
        dp[i] = [(dp[i-1][1]+dp[i-1][2]) % divider, (dp[i-2][0]+dp[i-2][2]) % divider, (dp[i-3][0]+dp[i-3][1]) % divider]

lt = []
for _ in range(int(input())):
    lt.append(int(input()))

maxlt = max(lt)
dp = [[0,0,0] for _ in range(maxlt + 1)]
dp[:4] = [0,0,0],[1,0,0],[0,1,0],[1,1,1]
solvemax(maxlt)
for e in lt:
    print(sum(dp[e]) % divider)
