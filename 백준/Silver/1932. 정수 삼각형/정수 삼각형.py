#1932
n = int(input())

tri = [[0]]
maxer = [[0]]

for i in range(n):
    tri.append([0] + list(map(int,input().split())) + [0])
    maxer.append([0 for _ in range(i+3)])

maxer[1][1] = tri[1][1]
for i in range(2,n+1):
    for j in range(1,i+1):
        maxer[i][j] = max(maxer[i-1][j-1],maxer[i-1][j]) + tri[i][j]

print(max(maxer[n]))