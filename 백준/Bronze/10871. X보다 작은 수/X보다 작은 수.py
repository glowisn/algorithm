#10871
N, X = map(int,input().split())
lst = list(map(int,input().split()))
for ls in lst:
    if ls < X:
        print(ls,end=' ')
print()