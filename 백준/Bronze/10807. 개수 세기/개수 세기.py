input()
lst = map(int,input().rsplit())
r = int(input())
count = 0
for i in lst:
    if i == r:
        count += 1

print(count)