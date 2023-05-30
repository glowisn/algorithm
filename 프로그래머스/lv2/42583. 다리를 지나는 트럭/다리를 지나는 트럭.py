from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bw = 0
    b = deque([0 for _ in range(bridge_length)])
    while trucks:
        time += 1
        #tik
        # Truck out
        t = b[-1]
        bw -= t
        b[-1] = 0
        # Truck Go
        b.rotate(1)
        # assert(b[0] == 0)
        # Truck in
        if trucks[0] + bw <= weight:
            t = trucks.popleft()
            b[0] = t
            bw += t
        # print(b)
    
    while not all(item == 0 for item in b):
        time += 1
        # Truck out
        b.pop()
        # print(b)
        
    return time