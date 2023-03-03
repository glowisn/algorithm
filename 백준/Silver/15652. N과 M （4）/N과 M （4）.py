#15652
n,m = map(int,input().rsplit())
arr = []

def dfs(num = 1):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(num, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs()
