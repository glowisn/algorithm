
p = list(map(int,input().split()))

def simpleSort():
  for i in range(0,4):
    if(p[i] > p[i+1]):
      p[i],p[i+1] = p[i+1],p[i]
      print(*p, sep=' ')

while(p != [1,2,3,4,5]):
  simpleSort()