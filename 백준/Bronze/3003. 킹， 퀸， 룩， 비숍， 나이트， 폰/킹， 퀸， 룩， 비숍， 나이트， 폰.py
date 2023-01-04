#3003
lst = list(map(int,input().split()))
pieces = [1,1,2,2,2,8]
for i in range(6):
    print(pieces[i] - lst[i],end=' ')