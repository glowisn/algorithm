#10870
fib = []
def make_fib():
    if(len(fib) == 0):
        fib.append(0)
    elif(len(fib) == 1):
        fib.append(1)
    else:
        fib.append(fib[-2] + fib[-1])

N = int(input())

for _ in range(N+1):
    make_fib()

print(fib[N])