#1874
def solve(a:list):
    ops = []
    stack = []
    curr = 0
    for num in a:
        if num > curr:
            while num > curr:
                curr += 1
                stack.append(curr)
                ops.append("+")

        if len(stack) != 0 and num == stack[-1]:
            stack.pop(-1)
            ops.append("-")

    # print("Stack:",stack)
    # print("Ops",ops)
    if stack:
        return ["NO"]
    else:
        return ops

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

u = solve(a)
for e in u:
    print(e)