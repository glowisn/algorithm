#11022
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    a,b = map(int,input().split())
    c = a+b
    print("Case #%d: %d + %d = %d" %(i+1,a,b,c))