#4796

#연속하는 P일 중, L일동안만 사용. V일짜리 휴가

def max_camp(L,P,V,case):
    time = 0
    while V >= P:
        V = V - P
        time += L
    time += min(L,V)
    print("Case " + str(case) + ": " + str(time))
    return

case = 1
while True:
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    max_camp(L,P,V,case)
    case += 1

