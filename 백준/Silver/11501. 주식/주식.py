#11501
from sys import stdin
input = stdin.readline

sum = 0
def solve(prices:list):
    if len(prices)== 0:
        return
    global sum
    m = max(prices)
    maxlastind = 0
    for i,v in enumerate(prices):
        if v == m:
            maxlastind = i
    for i in range(maxlastind):
        if prices[i] < m:
            sum += m - prices[i]
    solve(prices[maxlastind+1:])

for _ in range(int(input())):
    N = int(input())
    prices = list(map(int,input().split()))
    solve(prices)
    print(sum)
    sum = 0