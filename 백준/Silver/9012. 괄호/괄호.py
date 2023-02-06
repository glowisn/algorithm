#9012
for _ in range(int(input())):
    flag = False
    stack = []
    for al in input():
        if al == '(':
            stack.append(al)
        elif al == ')':
            try:
                tmp = stack.pop(0)
            except:
                print("NO")
                flag = True
                break
    if flag:
        continue
    if stack:
        print("NO")
        continue
    else:
        print("YES")