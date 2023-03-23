#1182
N,S = map(int,input().rsplit())
arr = list(map(int,input().rsplit()))
arr.sort()
ans = 0

def solve(ind=0,summ = 0):
    global ans
    if ind == N:
        return

    summ += arr[ind]
    if summ == S:
        ans += 1

    solve(ind+1,summ)
    solve(ind+1,summ-arr[ind])

solve()

print(ans)
    
    