from collections import deque

def bfs(root:int,mat:list):
    visited = []
    queue = deque([root])
    
    while queue:
        t = queue.popleft()
        visited.append(t)
        
        for num in mat[t]:
            if num not in visited:
                queue.append(num)

    return len(visited)

def solution(n, wires):
    answer = 101
    mat = [[] for _ in range(n+1)]
    for i,j in wires:
        mat[i].append(j)
        mat[j].append(i)
        
    
    for i,j in wires:
        # cut
        mat[i].remove(j)
        mat[j].remove(i)
        # calculate
        answer = min(answer,abs(bfs(i,mat)-bfs(j,mat)))
        # reconnect
        mat[i].append(j)
        mat[j].append(i)
    

    return answer