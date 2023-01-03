#25501

def recursion(s:str,depth:int):
    if len(s) == 1 or len(s) == 0:
        return "1 " + str(depth)
    elif s[0] != s[-1]:
        return "0 " + str(depth)
    else:
        return recursion(s[1:-1],depth+1)

T = int(input())
for _ in range(T):
    print(recursion(input(),1))