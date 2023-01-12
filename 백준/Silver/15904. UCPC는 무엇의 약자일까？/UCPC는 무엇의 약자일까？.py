strr = input()
word = "UCPC"

i = 0
for al in strr:
    if al == word[i]:
        i += 1
        if i == 4:
            break

if i == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")


