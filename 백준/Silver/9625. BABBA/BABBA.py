#9625
k = int(input())
lst = [[] for _ in range(k+1)]
if k == 1:
    print(0,1)
elif k == 2:
    print(1,1)
else:
    lst[1] = [0,1]
    lst[2] = [1,1]
    for i in range(3,k+1):
        c = []
        for x,y in zip(lst[i-2],lst[i-1]):
            c.append(x+y)
        lst[i] = c
    print(*lst[k])