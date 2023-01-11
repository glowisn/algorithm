#1259
def isPelindrome(word:str):
    for i in range(len(word) // 2):
        if word[-(i+1)] != word[i]:
            return "no"
    return "yes"

while True:
    num = input()
    if num == '0':
        break
    print(isPelindrome(num))