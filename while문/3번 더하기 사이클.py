N = int(input())
cycle = 0
M = -1
#N이 0일 경우 값이 같게 되어 while문이 돌지 않을 것을 방지함
if N < 10:
    N = N * 10

n = N

while M != N:
    M = n%10*10 + (int(n/10) + n%10)%10
    #파이썬에서 n/10을 하면 자동으로 소수계산까지 해버리기 때문에 그 형을 제대로 정해주어야 함
    n = M
    cycle = cycle + 1

print(cycle)