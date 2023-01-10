#16953

astr,bstr = map(str,input().split())

cnt = 0
while int(astr) <= int(bstr):
    cnt += 1
    if int(astr) == int(bstr):
        print(cnt)
        quit()
    if bstr[-1] == '1':
        bstr = bstr[:-1]
    elif int(bstr) % 2 == 0:
        bstr = str(int(bstr) // 2)
    else:
        print(-1)
        quit()

print(-1)