#1629
def solve(a,b,c):
    if b == 1:
        return a % c
    else:
        t = solve(a,b//2,c)
        if b % 2 == 0:
            return (t * t) % c
        else:
            return (t * t * a) % c

a,b,c = map(int,input().split())
print(solve(a,b,c))