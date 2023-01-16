#11053
size = int(input())

arr = list(map(int,input().split()))

def lis(arr,n):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

print(lis(arr,size))
