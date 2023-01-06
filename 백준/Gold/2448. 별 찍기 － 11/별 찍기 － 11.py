# 2448
import sys
sys.setrecursionlimit(10**6)

def recursion(n):
    if n == 3:
        return ["  *  "," * * ","*****"]

    stars = recursion(n//2)
    L = []
    for s in stars:
        L.append(" " *(n//2) + s + " "*(n//2))
    for s in stars:
        L.append(s + " " +s)
    return L

N = int(input())

page = []

page = recursion(N)

print('\n'.join(page))
