#11729
def hanoi(num,from_,to_,via_):
    global moves
    if num == 1:
        # print(from_,to_)
        moves.append([from_,to_])
    else:
        hanoi(num-1,from_,via_,to_)
        # print(from_,to_)
        moves.append([from_,to_])
        hanoi(num-1,via_,to_,from_)

N = int(input())
moves = []

hanoi(N,1,3,2)

print(len(moves))
for move in moves:
    print(*move)