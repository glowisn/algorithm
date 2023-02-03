def knapsack2(n, W, w, v):
    memo = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i - 1] > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], v[i - 1] + memo[i - 1][j - w[i - 1]])
    
    return memo[n][W]

n,k = map(int,input().split())
w,v = [],[]
for _ in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)

print(knapsack2(n,k,w,v))
