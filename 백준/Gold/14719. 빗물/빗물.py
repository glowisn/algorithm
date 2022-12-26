# 14719

map(int, input().split())
lands = list(map(int, input().split()))

hill = lands[0]
hillindex = 0
tmpwater = 0
water = 0

maxhill = max(lands)
maxhillindex = 0
for i in range(len(lands)):
    if (maxhill == lands[i]):
        maxhillindex = i


# print("maxhillindex:",maxhillindex)
for i in range(maxhillindex + 1):
    # first case
    if i == 0:
        continue

    # normal case : filling water to right
    if lands[i] < hill:
        tmpwater += (hill-lands[i])
    # normal case : new hill, water in
    elif lands[i] >= hill:
        water += tmpwater
        tmpwater = 0
        hill = lands[i]
        hillindex = i

rightlands = lands[maxhillindex:]
rightlands.reverse()

# print("rightlands: ", rightlands)
tmpwater = 0
hill = rightlands[0]
for i in range(len(rightlands)):
    # first case
    if i == 0:
        continue

    # normal case : filling water to right
    if rightlands[i] < hill:
        tmpwater += (hill-rightlands[i])
    # normal case : new hill, water in
    elif rightlands[i] >= hill:
        water += tmpwater
        tmpwater = 0
        hill = rightlands[i]
        hillindex = i


print(water)
