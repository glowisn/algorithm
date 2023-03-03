#15654
n,m = map(int,input().rsplit())
s = list(map(int,input().rsplit()))
s.sort()
used = [0 for _ in range(n)]

def dfs(used,chosen = []):
    if len(chosen) == m:
        print(' '.join(map(str,chosen)))
        return
    
    for i in range(n):
        if not used[i]:
            chosen.append(s[i])
            used[i] = 1
            dfs(used,chosen)
            used[i] = 0
            chosen.pop()

dfs(used)
