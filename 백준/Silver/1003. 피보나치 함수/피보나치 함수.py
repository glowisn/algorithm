#1003
nums = []
for _ in range(41):
    nums.append([])

nums[0] = [1,0]
nums[1] = [0,1]

def hash(n:int):
    global nums
    if nums[n]:
        return nums[n]
    else:
        return False

def fib(n:int):
    global nums
    if hash(n):
        return hash(n)
    else:
        nums[n] = [fib(n-2)[0] +fib(n-1)[0],fib(n-2)[1] + fib(n-1)[1]]
        return hash(n)

for _ in range(int(input())):
    print(*fib(int(input())))