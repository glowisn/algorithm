#11051
#nCk
n,k=map(int,input().split())
mul = 1
div = 1
for i in range(k):
    mul = (mul * (n-i)) 
    div = (div * (k-i))

print(mul//div % 10007)