#2810

n = int(input())
seats = input()

lflag = True
cnt = 0
i = 0
while True:
    if seats[i] == 'S':
        cnt += 1
    if seats[i] == 'L':
        if lflag:
            cnt += 2
            i += 1
            lflag = False
        else:
            cnt += 1
            i += 1
    i += 1
    if n == i:
        break

print(cnt)
        
    
            
