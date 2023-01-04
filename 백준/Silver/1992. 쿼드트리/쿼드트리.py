#1992

def recursion(vid:list,n:int):
    if n == 1:
        return str(vid[0][0])
    if all(0 not in l for l in vid):
        return "1"
    elif all(1 not in l for l in vid):
        return "0"
    else:
        opt = ""
        tmp = []
        for i in range(n//2):
            tmp.append(vid[i][0:n//2])
        opt += recursion(tmp,n//2)
        tmp.clear()
        for i in range(n//2):
            tmp.append(vid[i][n//2:])
        opt += recursion(tmp,n//2)
        tmp.clear()
        for i in range(n//2,n):
            tmp.append(vid[i][0:n//2])
        opt += recursion(tmp,n//2)
        tmp.clear()
        for i in range(n//2,n):
            tmp.append(vid[i][n//2:])
        opt += recursion(tmp,n//2)
        
        return "(" + opt + ")"

N = int(input())
arr = []
for i in range(N):
    tp = str(input())
    ar = []
    for a in tp:
        ar.append(int(a))
    arr.append(ar)

print(recursion(arr,N))