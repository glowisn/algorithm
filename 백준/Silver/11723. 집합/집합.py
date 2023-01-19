#11723
from sys import stdin
input = stdin.readline

s = set()
dft = {i for i in range(1,21)}
for _ in range(int(input())):
    command = list(input().split())
    match command[0]:
        case "add":
            s.add(int(command[1]))
        case "remove":
            try:
                s.remove(int(command[1]))
            except:
                continue
        case "check":
            print(1) if int(command[1]) in s else print(0)
        case "toggle":
            try:
                s.remove(int(command[1])) if int(command[1]) in s else s.add(int(command[1]))
            except:
                continue
        case "all":
            s = dft
        case "empty":
            s.clear()

