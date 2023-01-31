#9655
def who_wins(n:int):
    if n % 2 == 0:
        return "CY"
    else:
        return "SK"

print(who_wins(int(input())))