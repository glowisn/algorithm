def solution(frame_count,recos):
    frames = []
    levels = [] 
    for reco in recos:
        if reco in frames:
            for i in range(len(frames)):
                if frames[i] == reco:
                    levels[i] += 1
        else:
            if len(frames) >= frame_count:
                min_l = min(levels)
                for j in range(frame_count):
                    if min_l == levels[j]:
                        frames.pop(j)
                        levels.pop(j)
                        break
                frames.append(reco)
                levels.append(1)
            else:
                frames.append(reco)
                levels.append(1)
    return frames




N = int(input())
M = int(input())
recos = map(int,input().rsplit())

t = solution(N,recos)
t.sort()

print(*t)