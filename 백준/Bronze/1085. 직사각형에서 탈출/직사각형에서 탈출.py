#1085
x,y,w,h = map(int,input().split())
lw = w - x
lh = h - y

print(min(x,y,lw,lh))