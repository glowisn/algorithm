#2675
for _ in range(int(input())):
    Rs, S = input().split()
    R = int(Rs)
    for ch in S:
        print(ch * R ,end='')
    print()