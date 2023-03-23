#25304
X = int(input())
for _ in range(int(input())):
    a,b = map(int,input().rsplit())
    X -= a * b

if X == 0:
    print("Yes")
else:
    print("No")