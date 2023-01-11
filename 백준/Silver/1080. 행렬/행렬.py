#1080

#flip 3x3 list from x,y
def conversion(lst:list,x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            lst[i][j] = (lst[i][j] + 1) % 2 #flip


#input
N,M = map(int,input().split())
a, b = [],[]
for _ in range(N):
    a.append([int(c) for c in input()])
for _ in range(N):
    b.append([int(c) for c in input()])


#Too small arguemnt
if N < 3 or M < 3:
    for i in range(N):
        for j in range(M):
            if a[i][j] != b[i][j]:
                print(-1)
                quit()
    print(0)
    quit()

cnt = 0

for i in range(N-2):
    for j in range(M-2):
        if a[i][j] != b[i][j]:
            conversion(a,i,j)
            cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)