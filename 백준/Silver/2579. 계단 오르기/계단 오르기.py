#2579

n = int(input())

if n == 1:
    print(int(input()))
    quit()
elif n == 2:
    print(int(input()) + int(input()))
    quit()
    
stairs =[int(input()) for _ in range(n)]

summ = [stairs[0],stairs[0] + stairs[1],max(stairs[0] + stairs[2], stairs[1] + stairs[2])]

for i in range(3,n):
    summ.append(max(summ[i-2] + stairs[i], summ[i-3] + stairs[i-1] + stairs[i]))

print(summ[-1])