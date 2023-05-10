#1929
m,n = map(int,input().split())
if n == 1:
    quit()
arr = [True] * (n+1)
arr[1] = False

for i in range(2,n+1):
    j = 2
    while i * j <= n:
        arr[i*j] = False
        j += 1

for i in range(m,n+1):
    if arr[i]:
        print(i)
