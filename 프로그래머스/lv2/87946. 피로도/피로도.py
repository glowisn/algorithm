from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in range(1,len(dungeons)+1):
        for item in permutations(dungeons,i):
            e = k
            count = 0
            for ite in item:
                if e >= ite[0]:
                    count += 1
                    e -= ite[1]
            answer = max(answer,count)
    return answer