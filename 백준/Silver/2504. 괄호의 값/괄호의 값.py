#2504
def getNumber(la):
    s = []
    ans = 0
    mul = 1
    for i in range(len(la)):
        if la[i] == '(':
            s.append(la[i])
            mul *= 2
        elif la[i] == '[':
            s.append(la[i])
            mul *= 3
        elif la[i] == ')':
            if s and s[-1] == '(':
                s.pop()
                if la[i-1] == '(':
                    ans += mul
                mul //= 2
            else:
                return 0
        elif la[i] == ']':
            if s and s[-1] == '[':
                s.pop()
                if la[i-1] == '[':
                    ans += mul
                mul //= 3
            else:
                return 0

    if(not s):
        return ans
    
    return 0

print(getNumber(list(input())))