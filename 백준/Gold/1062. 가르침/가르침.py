#1062
from itertools import combinations
import sys

n, k = map(int,input().split())
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def check(learned:list,alphlist:list):
    ans = 0
    for alphs in alphlist:
        readable = 1
        # {b,e}
        for alph in alphs:
            # b
            if learned[ord(alph)] == 0:
                readable = 0
                break
        if readable == 1:
            ans += 1
    return ans

if k < 5:
    print(0)
else:
    k -= 5

    #anta tica
    alph = {'a','n','t','i','c'}

    k_list = set(chr(i) for i in range(97, 123)) - alph

    learned = [0] * 123
    for x in alph:
        learned[ord(x)] = 1

    maxnum = 0

    for teach in list(combinations(k_list,k)):
        for t in teach:
            learned[ord(t)] = 1
        comnum = check(learned,words)
        if comnum > maxnum:
            maxnum = comnum
        for t in teach:
            learned[ord(t)] = 0

    print(maxnum)
            