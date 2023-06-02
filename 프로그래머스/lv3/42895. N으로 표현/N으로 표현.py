def cal(X,Y):
    n = set()
    for x in X:
        for y in Y:
            n.add(x+y)
            n.add(x-y)
            n.add(x*y)
            if y != 0:
                n.add(x//y)
    return n

def solution(N, k):
    if N == k:
        return 1
    r = {}
    r[1] = {N}
    for n in range(2,9):
        t = {int(str(N)*n)}
        i = 1
        while i < n:
            t.update(cal(r[i],r[n-i]))
            i += 1
            
        if k in t:
            return n
        
        r[n] = t
    
         
    return -1