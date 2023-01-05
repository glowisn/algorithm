#9148
from sys import stdin
input = stdin.readline

table = {}

def hash(a,b,c):
    global table
    if a <= 0 or b <= 0 or c <= 0:
        return table[(0,0,0)]
    if (a,b,c) in table:
        return table[(a,b,c)]
    elif (a,b,c) not in table:
        return None

def calculate(a,b,c):
    global table
    if hash(a,b,c) != None:
        return hash(a,b,c)

    if a < b and b < c:
        if hash(a,b,c-1) == None:
            calculate(a,b,c-1)
        if hash(a,b-1,c-1) == None:
            calculate(a,b-1,c-1)
        if hash(a,b-1,c) == None:
            calculate(a,b-1,c)

        table[(a,b,c)] = hash(a, b, c-1) + hash(a, b-1, c-1) - hash(a, b-1, c)

    else:
        if hash(a-1,b,c) == None:
            calculate(a-1,b,c)
        if hash(a-1,b-1,c) == None:
            calculate(a-1,b-1,c)
        if hash(a-1,b,c-1) == None:
            calculate(a-1,b,c-1)
        if hash(a-1,b-1,c-1) == None:
            calculate(a-1,b-1,c-1)

        table[(a,b,c)] = hash(a-1, b, c) + hash(a-1, b-1, c) + hash(a-1, b, c-1) - hash(a-1, b-1, c-1)

    return table[(a,b,c)]

def w(a,b,c):
    global table
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    return calculate(a,b,c)
                
            
table[(0,0,0)] = 1
while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        quit()
    print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(w(a,b,c)))