#3568
a = input().rsplit()

master = a[0]
subs = []
tps = []
for vars in a[1:]:
    stack = []
    name = ''
    for s in vars:
        if s.isalpha():
            name += s
        elif s == '*':
            stack.append(s)
        elif s == '&':
            stack.append(s)
        elif s == '[':
            stack.append('[]')
        elif s == ']':
            continue
        else:
            continue
    subs.append(name)
    tps.append(stack[::-1])            

for i in range(len(subs)):
    print(master,end='')
    print(*tps[i],sep='',end=' ')
    print(subs[i],end='')
    print(';')