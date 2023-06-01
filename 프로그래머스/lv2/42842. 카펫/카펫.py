def solution(brown, yellow):
    r = (brown + 4) // 2
    for i in range(3, r//2 + 1):
        if (r - i - 2) * (i - 2) == yellow:
            return [r-i,i]