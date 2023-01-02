#24060
from sys import stdin
input = stdin.readline

count = 0

def merge(p:int,q:int,r:int):
    global A
    global K
    global count
    i = p
    j = q+1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    # left remain
    while i <= q:
        tmp.append(A[i])
        i += 1
    # right remain
    while j <= r:
        tmp.append(A[j])
        j += 1
    #put to A COUNT HERE
    i = p
    for t in range(len(tmp)):
        A[i] = tmp[t]
        count += 1
        if count == K:
            print(A[i])
            quit()
        i += 1



def merge_sort(p:int,r:int):
    if p < r:
        q = (p + r) // 2
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)

N, K = map(int,input().split())

A = list(map(int,input().split()))

merge_sort(0,N-1)

print('-1')