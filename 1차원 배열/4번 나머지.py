array = []

for n in range(0, 10):
    A = int(input())

    A = A%42

    if A not in array:
        array.append(A)

print(len(array))