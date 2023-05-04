#4673
from sys import stdout
# print = stdout.write

dnum = set([])

for i in range(1,10001):
    tmp = i
    stt = str(i)
    for st in stt:
        tmp += int(st)
    dnum.add(tmp)

for i in range(1,10001):
    if i in dnum:
        continue
    else:
        print(i)