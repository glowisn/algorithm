#16506
import sys
input = sys.stdin.readline

n = int(input().rstrip())
assemblies = []
for _ in range(n):
    tmp = input().rstrip().split()
    assemblies.append([tmp[0]] + list(map(int,tmp[1:])))

ans = []

for asb in assemblies:
    ops = ''
    cacheFlag = False
    #check cache
    if asb[0][-1] == 'C':
        cacheFlag = True
    #check opCode
    if asb[0][:3] == 'ADD':
        ops = '0000'
    elif asb[0][:3] == 'SUB':
        ops = '0001'
    elif asb[0][:3] == 'MOV':
        ops = '0010'
    elif asb[0][:3] == 'AND':
        ops = '0011'
    elif asb[0][:2] == 'OR':
        ops = '0100'
    elif asb[0] == 'NOT':
        ops = '0101'
    elif asb[0][:4] == 'MULT':
        ops = '0110'
    elif asb[0][:5] == 'LSFTL':
        ops = '0111'
    elif asb[0][:5] == 'LSFTR':
        ops = '1000'
    elif asb[0][:5] == 'ASFTR':
        ops = '1001'
    elif asb[0][:2] == 'RL':
        ops = '1010'
    elif asb[0][:2] == 'RR':
        ops = '1011'
    
    if cacheFlag:
        ops += '1'
    else:
        ops += '0'
    
    #5
    ops += '0'

    rD = str(bin(asb[1]))[2:].zfill(3)
    ops += rD

    rA = str(bin(asb[2]))[2:].zfill(3)
    ops += rA

    rB = ''
    if cacheFlag:
        rB = str(bin(asb[3]))[2:].zfill(4)
    else:
        rB = str(bin(asb[3]))[2:].zfill(3) + '0'
    
    ops += rB
    
    ans.append(ops)

print(*ans,sep='\n')
