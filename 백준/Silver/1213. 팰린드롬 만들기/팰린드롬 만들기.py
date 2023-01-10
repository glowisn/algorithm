#1231
name = input()
alpcnt = []
for _ in range(26):
    alpcnt.append(0)
for al in name:
    alpcnt[ord(al) - 65] += 1

# print(alpcnt)

oddcnt = 0
oddflag = -1
for i in range(26):
    if alpcnt[i] % 2 != 0:
        oddcnt += 1
        if oddcnt > 1:
            print("I'm Sorry Hansoo")
            quit()
        oddflag = i
        alpcnt[i] = alpcnt[i] - 1
    alpcnt[i] = alpcnt[i] // 2

# print(oddcnt)
# print(oddflag)
# print(alpcnt)

pel = []
t = ''
for j in range(26):
    while alpcnt[j] > 0:
        t = chr(j + 65)
        print(t,end='')
        pel.append(t)
        alpcnt[j] -= 1

#print oddcnt if exist
if oddflag != -1:
    print(chr(65 + oddflag),end='')

pel.reverse()
for p in pel:
    print(p,end='')
print()