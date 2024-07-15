blocks = {
    'P': 2,
    'C': 2,
    'A': 1,
    'D': 0
}
qt = int(input())
relation = input()
distance = 0
for i in relation:
    distance += blocks[i]
print(distance)