def solution(brown, yellow):
    r = (brown + 4) // 2
    for i in range(3, r//2 + 1):
        h = i - 2
        w = r - i - 2
        if w * h == yellow:
            return [w+2,h+2]
    return []