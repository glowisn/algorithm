#11021
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    print("Case #"+str(i+1)+": "+str(sum(map(int,input().rsplit()))))