#6603

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result

def do():
    s = list(map(int,input().split()))
    k = s.pop(0)
    if k == 0:
        return 0
    for e in gen_combinations(s,6):
        print(*e)
        
    

while(1):
    stop = do()
    if stop == 0:
        quit()
    print()