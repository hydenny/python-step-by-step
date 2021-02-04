def d(n):
    sum = n

    while n > 0:
        sum = sum + n%10
        n = int(n/10)

    return sum

list = [0]

list = list * 20000
#10000 이하의 수 중에서 셀프 넘버를 구하는건데, 100의 경우 101과 99가 둘 다 생성자에 해당하는 것을 생각해,
# #10000이 넘는 수도 그 보다 작은 수의 생성자가 될 수 있음을 알아야 함

i = 1

while d(i) < 20000:
    list[d(i)-1] = 1
    i += 1

j = 0

for j in range(10000):
    if list[j] == 0:
        print(j+1)