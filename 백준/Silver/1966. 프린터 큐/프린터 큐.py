#1966
def solve(N,M:int,I:list):
    cnt = 0
    while I:
        if max(I) > I[0]:
            I.append(I.pop(0))
        else:
            I.pop(0)
            cnt += 1
            if M == 0:
                return cnt
        if M == 0:
            M = len(I)-1
        else:
            M -= 1
    return cnt

for _ in range(int(input())):
    N,M = map(int,input().split())
    I = list(map(int,input().split()))
    print(solve(N,M,I))