#1912
n = int(input())
arr = list(map(int,input().split()))
maxx = [arr[0]]
for i in range(1,n):
    maxx.append(max(maxx[i-1] + arr[i], arr[i]))
print(max(maxx))