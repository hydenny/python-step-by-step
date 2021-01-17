T = int(input())
n = 1

for T in range(0, T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #" + str(n) + ": " + str(A) + " + " + str(B) + " = " + str(A+B))
    n = n + 1