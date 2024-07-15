A = int(input())
B, C, D = map(int,input().split())
if A > B or A > C or A > D:
    print("N")
else:
    print("S")