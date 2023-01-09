#1789

s = int(input())
curr = 0
i = 1

while True:
    curr += i
    if curr > s:
        break
    i += 1

print(i - 1)