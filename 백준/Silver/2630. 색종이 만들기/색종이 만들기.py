#2630
zeros, ones = 0, 0

def divide(page:list):
    half = len(page) // 2
    s_1,s_2,s_3,s_4 = [],[],[],[]
    for i in range(half):
        s_1.append(page[i][:half])
        s_2.append(page[i][half:])
    for i in range(half,half*2):
        s_3.append(page[i][:half])
        s_4.append(page[i][half:])
    return s_1,s_2,s_3,s_4

def recursion(page:list,N):
    global zeros, ones
    if all(0 not in l for l in page):
        ones += 1
        return 
    if all(1 not in l for l in page):
        zeros += 1
        return
    
    else:
        for e in divide(page):
            recursion(e,N//2)
    

N = int(input())
page = [list(map(int,input().split())) for _ in range(N)]
recursion(page,N)
print(zeros)
print(ones)