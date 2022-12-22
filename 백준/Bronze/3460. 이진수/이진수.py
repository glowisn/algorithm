#3460

def do2div(num):
    bi = str(bin(num))
    bi = bi[2:]
    bi = bi[::-1]
    for i in range(len(bi)):
        if(bi[i] == '1'):
            print(i, end=' ')
    print()


for _ in range(int(input())):
    do2div(int(input()))