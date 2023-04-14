from sys import stdin
input = stdin.readline


n = int(input().rstrip())
graph = [list(map(int, input().rsplit())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 

for i in range(n):
    for j in range(n):

        if graph[i][j] == 0:
            continue

        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]

        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]

print(dp[-1][-1])