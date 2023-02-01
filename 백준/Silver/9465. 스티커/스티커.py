#9465
from sys import stdin
input = stdin.readline

#dp[i] = max( dp[i-1] + A  )

def solve():
    n = int(input())
    a = [0] + list(map(int,input().split()))
    b = [0] + list(map(int,input().split()))

    if n < 2:
        return max(a+b)
    
    dpa = [0 for _ in range(n+1)]
    dpb = [0 for _ in range(n+1)]

    dpa[1],dpb[1] = a[1],b[1]
    dpa[2],dpb[2]= b[1] + a[2], a[1] + b[2]

    for i in range(3,n+1):
        dpa[i] = max(dpa[i-2],dpb[i-2],dpb[i-1]) + a[i]
        dpb[i] = max(dpa[i-2],dpa[i-1],dpb[i-2]) + b[i]

    # print("dpa:",dpa)
    # print("dpb:",dpb)
    return max(dpa+dpb)


for _ in range(int(input())):
    print(solve())