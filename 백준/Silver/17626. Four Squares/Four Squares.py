#17636
def main():
    n=int(input())
    l=[i*i for i in range(1,224)]
    for i in range(223):
        e1=l[i]
        if e1==n:
            return 1

    for i1 in range(223):
        e1=l[i1]
        for i2 in range(i1,223):
            e2=l[i2]
            if e1+e2==n:
                return 2
                
    for i1 in range(223):
        e1=l[i1]
        for i2 in range(i1,223):
            e2=l[i2]
            for i3 in range(i2,223):
                e3=l[i3]
                if e1+e2+e3==n:
                    return 3
    return 4

print(main())