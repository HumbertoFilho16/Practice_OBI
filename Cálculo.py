L = int(input())
Count = 0
bacteria = []
best = 0
ratio = 0

while Count < L:
    c, d = map(int,input().split())
    bacteria.append([c,d])                    
    Count += 1

for i, j in enumerate(bacteria):
    mult = j[0] ** j[1]
    if mult > ratio:
        ratio = mult
        best = i
    else:
        continue

print(best)