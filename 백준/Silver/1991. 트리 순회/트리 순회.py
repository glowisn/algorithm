#1991

N = int(input())

tree = {}

for i in range(N):
    parent ,left, right = map(str,input().split())
    tree[parent] = [left,right]

def prefix(node):
    if node != '.':
        print(node,end='')
        prefix(tree[node][0])
        prefix(tree[node][1])

prefix('A')
print()

def midfix(node):
    if node != '.':
        midfix(tree[node][0])
        print(node,end='')
        midfix(tree[node][1])

midfix('A')
print()

def postfix(node):
    if node != '.':
        postfix(tree[node][0])
        postfix(tree[node][1])
        print(node,end='')

postfix('A')
print()

