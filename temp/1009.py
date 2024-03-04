#1009

def solve(a, b):
    b = b % 4 if b % 4 != 0 else 4 
    c = a % 10
    result = 1 
    for _ in range(b): 
        result = (result * c) % 10
    return result if result != 0 else 10

t = int(input())
for _ in range(t):
    print(solve(*map(int, input().split())))


