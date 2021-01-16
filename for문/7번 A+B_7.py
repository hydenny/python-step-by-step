T = int(input())
n = 1
for T in range(0, T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #" + str(n) + ": " + str(A+B))
    #print문에서는 str형만 concatenate가 가능하므로, 형변환을 꼭 해줘야 함.
    n = n + 1
