import sys

m = int(sys.stdin.readline())

ms = set()

def operate(s):
    global ms
    if (s[0] == 'add'):
        ms.add(int(s[1]))
    if (s[0] == 'remove'):
        x = int(s[1])
        if x in ms:
            ms.remove(x)
    if (s[0] == 'check'):
        x = int(s[1])
        if x in ms:
            print(1)
        else:
            print(0)
    if (s[0] == 'toggle'):
        x = int(s[1])
        if x in ms:
            ms.remove(x)
        else:
            ms.add(x)
    if (s[0] == 'all'):
        ms = {i for i in range(1, 21)}
    if (s[0] == 'empty'):
        ms = set()


for _ in range(m):
  s = sys.stdin.readline().strip().split()
  operate(s)
