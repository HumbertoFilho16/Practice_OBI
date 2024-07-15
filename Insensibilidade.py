jones = int(input())
count = 0
insen = 0

while count < jones:
    A, B, C, D = map(int,input().split())
    X = A - C
    Y = B - D
    if X < 0:
        X = X * (-1)
    if Y < 0:
        Y = Y * (-1)
    insen = insen + X * X + Y * Y
    count += 1

print(insen)
    