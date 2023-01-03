# 10994
import sys
sys.setrecursionlimit(10**6)

def recursion(n):
    if n == 1:
        return ['*']
    
    tmp = []
    tmp.append('*' * (n * 4 - 3))
    tmp.append('*' + ' ' * (n * 4 - 5) + '*')
    for rec in recursion(n-1):
        tmp.append('* ' + rec + ' *')
    tmp.append('*' + ' ' * (n * 4 - 5) + '*')
    tmp.append('*' * (n * 4 - 3))
    return tmp

print('\n'.join(recursion(int(input()))))
