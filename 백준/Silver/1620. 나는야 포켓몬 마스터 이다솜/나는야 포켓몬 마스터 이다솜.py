#1620
import sys
input = sys.stdin.readline
N,M = map(int,input().rsplit())
dic = dict()
for i in range(1,N+1):
    dic[i] = input().rstrip()
rdic = {v:k for k,v in dic.items()}
for _ in range(M):
    r = input().rstrip()
    try:
        t = int(r)
        print(dic[t])
    except:
        print(rdic[r])
