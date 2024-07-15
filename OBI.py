COMP, POINTS = map(int,input().split())
count = 0
quant = 0
while count < COMP:
    A, B = map(int,input().split())
    sume = A + B
    if sume >= POINTS:
        quant += 1
    count += 1
print(quant)


