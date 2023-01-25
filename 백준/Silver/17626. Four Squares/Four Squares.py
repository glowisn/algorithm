#17626
n = int(input())
a = [0,1]

for i in range(2,n+1):
    min_val = 1e9
    j = 1
    while (j**2) <= i:
        min_val = min(min_val,a[i - (j**2)])
        j += 1
    a.append(min_val + 1)
print(a[n])
