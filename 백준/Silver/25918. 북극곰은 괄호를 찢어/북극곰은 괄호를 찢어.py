#25918
n = int(input())
s = list(input())

def check(s,piv):
    cnt = 0
    maxx = 0
    for al in s:
        if piv == al:
            cnt += 1
            if maxx < cnt:
                maxx = cnt
        else:
            cnt -= 1
    return maxx



if s.count('(') != s.count(')'):
    print(-1)
    quit()

t = max(check(s,'('),check(s,')'))

print(t)