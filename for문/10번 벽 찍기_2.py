N = int(input())
a = N

for N in range(1, N+1):
    print(' '*(a-1) + '*'*N)
    a = a - 1