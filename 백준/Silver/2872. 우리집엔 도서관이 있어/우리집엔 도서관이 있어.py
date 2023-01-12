#2872
from sys import stdin
input = stdin.readline

n = int(input())
books = [int(input()) for _ in range(n)]

maxbook = n
for book in books[::-1]:
    if book == maxbook:
        maxbook -= 1
print(maxbook)