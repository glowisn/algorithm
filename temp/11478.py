origString = input().rstrip()
sett = set()

for i in range(len(origString)):
    for j in range(i, len(origString)):
        sett.add(origString[i:j+1])

print(len(sett))