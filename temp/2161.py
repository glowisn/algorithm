from collections import deque

deck = [i for i in range(1,int(input())+1)]

deck = deque(deck)

spare = []

while len(deck) != 1:
  spare.append(deck.popleft())
  deck.rotate(-1)


print(*spare,deck[0])
