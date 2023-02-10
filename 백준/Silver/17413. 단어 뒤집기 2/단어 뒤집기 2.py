#17413
from sys import stdin
input = stdin.readline

def printS(stack:list):
    while stack:
        print(stack.pop(),end='')
    return stack
        

s = input().rstrip()
stack = []
stackFlag = True
for al in s:
    if al == ' ':
        stack = printS(stack)
        print(al,end='')
    elif al == '<':
        stack = printS(stack)
        stackFlag = False
        print(al,end='')
    elif al == '>':
        stackFlag = True
        print(al,end='')
    else: # normal input
        if stackFlag:
            stack.append(al)
        else:
            print(al,end='')


stack = printS(stack)
print()