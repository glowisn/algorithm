#10610

N = list(str(input()))

sum = 0
zeroFlag = False
for n in N:
    if n == '0':
        zeroFlag = True
    sum += int(n)

if sum % 3 == 0 and zeroFlag:
    N.sort(key=lambda x: int(x))
    N.reverse()
    print(''.join(N))
else:
    print(-1)