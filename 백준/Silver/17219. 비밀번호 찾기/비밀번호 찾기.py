#17219
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

n, m = map(int,input().split())

dic = {}

for _ in range(n):
    ido,pwd = map(str,input().split())
    dic[ido] = pwd

outputstr = ""
for _ in range(m):
    outputstr += dic[input().rstrip()] + "\n"

print(outputstr)