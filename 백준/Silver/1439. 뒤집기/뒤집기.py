#1439

S = input()

piv = S[0]
curr = ''
cnt = 0
for al in S:
    if al != piv and al != curr:
        cnt += 1

    curr = al
    

print(cnt)