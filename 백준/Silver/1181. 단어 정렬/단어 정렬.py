#1181
from sys import stdin
input = stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

words = list(set(words))

words.sort(key=lambda x:(len(x),x))

for word in words:
    print(word)