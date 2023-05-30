import heapq

def mix(sco:heapq):
    a = heapq.heappop(sco)
    b = heapq.heappop(sco)
    heapq.heappush(sco,a + 2*b)
    
    return sco
    
    
def solution(sco, K):
    heapq.heapify(sco)
    time = 0
    while any(item < K for item in sco):
        time += 1
        if len(sco) == 1:
            return -1
        sco = mix(sco)
    
    return time