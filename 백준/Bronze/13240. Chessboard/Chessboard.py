n, m = map(int, input().split())

for nn in range(1, n + 1):
    for mm in range(1, m + 1):
        if ((nn + mm) % 2 == 0):
            print('*', end='')
        else:
            print('.', end='')
    print('')
