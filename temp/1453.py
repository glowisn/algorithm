#1453

people = int(input())
seats = list(map(int, input().split()))
duplicates = []

for i in range(people):
    if seats[i] in seats[i+1:]:
        duplicates.append(seats[i])

print(len(duplicates))