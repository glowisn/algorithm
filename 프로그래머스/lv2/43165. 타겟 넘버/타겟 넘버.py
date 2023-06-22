from copy import deepcopy
targ = 0
answer = 0

def cstack(numbers,sum):
    global answer, targ
    nnumbers = deepcopy(numbers)
    
    if len(nnumbers) == 0:
        if sum == targ:
            answer += 1
    else:
        t = nnumbers.pop()
        cstack(nnumbers,sum + t)
        cstack(nnumbers,sum - t)


def solution(numbers, target):
    global answer,targ
    answer = 0
    targ = target
    cstack(numbers,0)
    
    return answer