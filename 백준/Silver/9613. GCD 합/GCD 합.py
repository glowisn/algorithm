#9613
from math import gcd
from itertools import combinations

def sumOfGCD(lst):
    sum = 0
    for i in list(combinations(lst,2)):
        sum += gcd(i[0],i[1]) 
    return sum


test = []

for _ in range(int(input())):
    # test.append(list(map(int,input().split())))
    tmp = list(map(int,input().split()))
    tmp.pop(0)
    print(sumOfGCD(tmp))
