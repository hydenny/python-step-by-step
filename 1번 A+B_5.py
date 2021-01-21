A, B = input().split()

A = int(A)
B = int(B)

while A != 0 and B != 0:
    #파이썬에서는 &&연산자를 쓰지 않고 and or not을 씀
    print(str(A+B))

    A, B = input().split()

    A = int(A)
    B = int(B)