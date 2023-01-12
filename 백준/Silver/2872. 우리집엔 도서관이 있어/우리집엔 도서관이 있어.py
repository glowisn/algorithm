#2872
from sys import stdin
input = stdin.readline

n = int(input())
books = [int(input()) for _ in range(n)]

maxbook = n
cnt = 0
for book in books[::-1]:
    if book == maxbook:
        cnt += 1
        maxbook -= 1

print(n - cnt)