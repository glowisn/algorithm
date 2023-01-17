#1010
def build(m:int,n:int):
    # mCn = m.**.n / n! 
    ret = 1
    for i in range(m,m-n,-1):
        ret *= i
    for j in range(1,n+1):
        ret //= j
    return ret

for _ in range(int(input())):
    n,m = map(int,input().split())
    print(build(m,n))