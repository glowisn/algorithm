#5639
import sys
input = sys.stdin.readline

class Element:
    def __init__(self,value,lower,upper):
        self.value = value
        self.lower = lower
        self.upper = upper

def po_solve(arr:list):
    if (len(arr) == 0):
        return
    
    global po
    stack = []
    stack.append(Element(arr[0],0,10**6))
    for e in arr[1:]:
        while e < stack[-1].lower or e > stack[-1].upper:
            po.append(stack.pop().value)
        if e < stack[-1].value:
            stack.append(Element(e,stack[-1].lower,stack[-1].value - 1))
        if e > stack[-1].value:
            stack.append(Element(e,stack[-1].value + 1,stack[-1].upper))
    for _ in range(len(stack)):
        po.append(stack.pop().value)

arr,po = [],[]
while True:
    try:
        arr.append(int(input()))
    except:
        break

po_solve(arr)

print(*po,sep='\n')
