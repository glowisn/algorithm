
def flattening(field,inventory,h):
    time = 0
    blocks = inventory
    for n in range(len(field)):
        for m in range(len(field[n])):
            f = field[n][m]
            if f > h:
                time += 2 * (f-h)
                blocks += (f-h)
            if f < h:
                time += (h-f)
                blocks -= (h-f)
    
    return time if blocks >= 0 else -1

def solution(field:list,inventory:int):
    min_time, answer_height = 2e9,-1
    min_h = min(min(x) for x in field)
    max_h = max(max(x) for x in field)

    for target_h in range(min_h,max_h+1):
        time = flattening(field,inventory,target_h)
        if time != -1 and time <= min_time:
            min_time = time
            answer_height = target_h

    return min_time, answer_height

N,M,B = map(int,input().rsplit())
field = []
for _ in range(N):
    field.append(list(map(int,input().rsplit())))

mt,ah = solution(field,B)

print(mt,ah)