#2839

N = int(input())

div = N // 5
rem = N % 5

if rem == 0:
    print(div)
elif rem == 1:
    if N > 5:
        print(div + 1)
    else:
        print(-1)
elif rem == 2:
    if N > 11:
        print(div + 2)
    else:
        print(-1)
elif rem == 3:
    print(div + 1)
elif rem == 4:
    if N > 8:
        print(div + 2)
    else:
        print(-1)