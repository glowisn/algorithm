#1780

def check_all_minus_one(page:list):
    for pag in page:
        for pa in pag:
            if pa != -1:
                return False
    return True
def check_all_zero(page:list):
    for pag in page:
        for pa in pag:
            if pa != 0:
                return False
    return True
def check_all_plus_one(page:list):
    for pag in page:
        for pa in pag:
            if pa != 1:
                return False
    return True

def divide(page:list,n):
    ice = n // 3
    s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9 = [],[],[],[],[],[],[],[],[]
    for i in range(ice):
        s_1.append(page[i][:ice])
        s_2.append(page[i][ice:ice*2])
        s_3.append(page[i][ice*2:ice*3])
    for i in range(ice,ice*2):
        s_4.append(page[i][:ice])
        s_5.append(page[i][ice:ice*2])
        s_6.append(page[i][ice*2:ice*3])
    for i in range(ice*2,ice*3):
        s_7.append(page[i][:ice])
        s_8.append(page[i][ice:ice*2])
        s_9.append(page[i][ice*2:ice*3])
    return s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9

m1, zero, p1 = 0, 0, 0

def recursion(page:list,n:int):
    global m1,zero,p1
    if check_all_minus_one(page):
        m1 += 1
        return
    if check_all_zero(page):
        zero += 1
        return
    if check_all_plus_one(page):
        p1 += 1
        return

    else:
        for e in divide(page,n):
            recursion(e,n//3)

n = int(input())
pagei = [list(map(int,input().split())) for _ in range(n)]

recursion(pagei,n)
print(m1,zero,p1,sep='\n')