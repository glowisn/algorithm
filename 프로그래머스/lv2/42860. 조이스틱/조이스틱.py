def getlr(name:str):
    max_value = len(name) - 1
    tname = list(name)
    tname[0] = 'A'
    lcount = 0
    ind = len(tname)-1
    while any(al!='A' for al in tname):
        tname[ind] = 'A'
        ind -= 1
        lcount += 1
    tname = list(name)
    tname[0] = 'A'
    rcount = 0
    ind = 0
    while any(al!='A' for al in tname):
        ind += 1
        tname[ind] = 'A'
        rcount += 1
    print(lcount,rcount)
    minlen = min(lcount,rcount)
        
    # get super 'A's
    maxx, t, maxlind = 0,0,0
    for i in range(len(name)):
        if i == 0:
            continue
        if name[i] == 'A':
            t += 1
        else:
            if maxx < t:
                maxlind = i
                maxx = t
            t = 0
    if maxx < t:
        maxlind = i+1
        maxx = t
    # super A is name[maxlind-maxx:maxlind]
    left = len(name) - maxlind
    right = max(maxlind-maxx - 1,0)
    # print(right*2+left,left*2+right,right,left)
    # print(max_value,minlen,left*2+right,right*2+left)
    return min(max_value,minlen,left*2+right,right*2+left)

def getud(name:str):
    s = 0
    for al in name:
        s += min(ord(al) - 65, abs(ord(al)- 65 - 26))
    return s

def solution(name):
    if all(al=='A' for al in name):
        return 0
    a = getud(name)
    b = getlr(name)
    # print(a,b)
    return a + b