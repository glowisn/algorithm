
T = int(input())

def put(key,dic:dict):
  if key in dic:
    dic[key] += 1
  else:
    dic[key] = 1

def solve():
  closet = dict()
  n = int(input())
  for i in range(n):
    name, typ = input().split()
    put(typ,closet)
  summ = 1
  for nums in closet.values():
    summ *= (nums+1)
  print(summ-1)



for _ in range(T):
  solve()