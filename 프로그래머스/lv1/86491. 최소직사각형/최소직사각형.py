from itertools import combinations

def solution(sizes):
    le = len(sizes)
    ls = []
    ss = []
    indexs = [i for i in range(le)]
    for w,h in sizes:
        if w < h:
            ss.append(w)
            ls.append(h)
        else:
            ls.append(w)
            ss.append(h)
    return max(ls) * max(ss)