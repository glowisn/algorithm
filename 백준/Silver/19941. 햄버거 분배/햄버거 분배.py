#19941
n, k = map(int,input().split())
bench = list(input())

# H: hamberger P: person O: empty plate F: full person

for i in range(len(bench)):
    if bench[i] == 'P':
        for hand in range(-k,k+1):
            if i + hand >= 0 and i + hand < len(bench): # index error cover
                if bench[i + hand] == 'H':
                    bench[i + hand] = 'O'
                    bench[i] = 'F'
                    break


# print(bench)

print(bench.count('F'))
