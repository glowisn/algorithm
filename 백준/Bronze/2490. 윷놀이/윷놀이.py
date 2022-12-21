# 2490

def yutCount(input):
    if (input == 4):
        return "D"
    elif (input == 3):
        return "C"
    elif (input == 2):
        return "B"
    elif (input == 1):
        return "A"
    else:
        return "E"


a = []
for _ in range(3):
    a.append(list(map(int, input().split())))

for i in range(3):
    print(yutCount(a[i].count(0)))
