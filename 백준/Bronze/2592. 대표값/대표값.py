#2592
from collections import Counter

arr= []
for _ in range(10):
    arr.append(int(input()))

print(sum(arr)//10)
print(Counter(arr).most_common()[0][0])