#15988
def solvemax(n:int)->int:
    global dp
    for i in range(4,n+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

lt = []
for _ in range(int(input())):
    lt.append(int(input()))

maxlt = max(lt)
dp = [0 for _ in range(maxlt+1)]
dp[:4] = 0,1,2,4
solvemax(maxlt)

for e in lt:
    print(dp[e])