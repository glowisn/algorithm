#15657
n,m = map(int,input().rsplit())
s = list(map(int,input().rsplit()))
s.sort()

def dfs(chosen=[]):
    if len(chosen) == m:
        print(' '.join(map(str,chosen)))
        return
    
    for i in range(n):
        if not chosen:
            chosen.append(s[i])
        else:
            if chosen[-1] <= s[i]:
                chosen.append(s[i])
            else:
                continue
        dfs(chosen)
        chosen.pop()

dfs()