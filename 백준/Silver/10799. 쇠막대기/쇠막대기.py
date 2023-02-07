#10799

a = input()
stack = []
ans = 0
prev = ''
for e in a:
    if e =='(':
        stack.append(e)
    elif e == ')':
        stack.pop(-1)
        if prev == e: # ))
            ans += 1
        else: # ()
            ans += len(stack)
    prev = e

print(ans)