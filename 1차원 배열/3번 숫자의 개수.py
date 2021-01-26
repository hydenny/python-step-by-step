A = int(input())
B = int(input())
C = int(input())

n = A * B * C

array = list(str(n))
#list 선언하는 방식.

for i in range(0, 10):
    print(array.count(str(i)))
    #list에서 특정 요소의 개수를 세주는 함수.