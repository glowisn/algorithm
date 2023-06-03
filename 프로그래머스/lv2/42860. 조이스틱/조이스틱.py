def getlr(name:str):
    min_move = len(name) - 1
    for i, c in enumerate(name):
        next_i = i+1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    return min_move

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
    print(a,b)
    return a + b