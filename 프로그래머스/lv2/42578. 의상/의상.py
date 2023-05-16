def solution(clothes):
    answer = 1
    # decompose
    closet = {}
    for itemname,itemtype in clothes:
        if itemtype in closet:
            closet[itemtype] += 1
        else:
            closet[itemtype] = 1
    
    # count
    for item, count in closet.items():
        answer *= (count + 1)
    return answer - 1