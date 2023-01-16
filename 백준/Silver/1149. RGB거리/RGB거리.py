#1149
n = int(input())

costs = [list(map(int,input().split())) for _ in range(n)]
summs = [costs[0]]


for i in range(1,n):
    summs.append([costs[i][0] +  min(summs[i-1][1] , summs[i-1][2]), costs[i][1] +  min(summs[i-1][0] , summs[i-1][2]),costs[i][2] +   min(summs[i-1][0] , summs[i-1][1])])

print(min(summs[i]))