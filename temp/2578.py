
board = [list(map(int,input().split())) for _ in range(5)]
check = [[0 for _ in range(5)] for _ in range(5)]

ans = []
for _ in range(5):
  ans += list(map(int,input().split()))

def find(num):
  for y in range(5):
    for x in range(5):
      if board[y][x] == num:
        check[y][x] = 1
        return

def checkN(num):
  bingos = 0
  find(num)
  for i in range(5):
    if all(check[i]):
      bingos += 1
  for j in range(5):
    if all(check[i][j] for i in range(5)):
        bingos += 1
  if all(check[i][i] for i in range(5)):
    bingos += 1
  if all(check[i][4-i] for i in range(5)):
    bingos += 1
  
  if bingos >= 3:
    return True
  return False

for i in range(len(ans)):
  if(checkN(ans[i])):
    print(i+1)
    break