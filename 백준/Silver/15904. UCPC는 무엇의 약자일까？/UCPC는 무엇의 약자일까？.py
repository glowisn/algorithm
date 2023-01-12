#15904
strr = input()

UCPC_flag = [False,False,False,False]
t = 0

for i in range(len(strr)):
    if strr[i] == 'U':
        UCPC_flag[0] = True
        t = i + 1
        break

for i in range(t,len(strr)):
    if strr[i] == 'C':
        UCPC_flag[1] = True
        t = i + 1
        break

for i in range(t,len(strr)):
    if strr[i] == 'P':
        UCPC_flag[2] = True
        t = i + 1
        break

for i in range(t,len(strr)):
    if strr[i] == 'C':
        UCPC_flag[3] = True
        t = i + 1
        break

if all(UCPC_flag):
    print("I love UCPC")
else:
    print("I hate UCPC")