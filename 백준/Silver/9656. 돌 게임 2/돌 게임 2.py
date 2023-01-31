#9656
def who_wins(n:int):
    if n % 2 == 0:
        return "SK"
    else:
        return "CY"

print(who_wins(int(input())))