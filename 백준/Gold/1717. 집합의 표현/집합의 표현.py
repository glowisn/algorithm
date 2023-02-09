#1717
import sys

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]
    

def union(a,b):
    a = find(a)
    b = find(b)
    #이 시점에서 a,b는 이미 대표값

    if a == b:
        return
    
    if rank[a] == rank[b]:
        rank[a] += 1
        arr[b] = a
    elif rank[a] > rank[b]:
        rank[b] = rank[a]
        arr[b] = a
    else: # rank[b] > rank[a]:
        rank[a] = rank[b]
        arr[a] = b

n,m = map(int,sys.stdin.readline().rsplit())
arr = [i for i in range(n+1)]
rank = [1 for _ in range(n+1)]
for _ in range(m):
    i,a,b = map(int,sys.stdin.readline().rsplit())
    if i == 0:
        union(a,b)
    elif i == 1:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")