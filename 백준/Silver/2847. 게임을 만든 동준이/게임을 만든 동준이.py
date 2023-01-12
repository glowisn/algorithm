#2847

N = int(input())

scores = [int(input()) for _ in range(N)]

scores.reverse()

maxx = scores[0]

summ = 0

for e in scores[1:]:
    maxx -= 1
    if e > maxx:
        summ += e - maxx
    else:
        maxx = e
    
print(summ)
