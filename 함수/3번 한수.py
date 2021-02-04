def f(n):

    result = True

    if n < 100:
        return result

    if n == 1000:
        result = False
        return result

    a = n//100
    b = (n//10)%10
    c = n%10

    if a-b != b-c:
        result = False

    return result

N = int(input())

count = 0

for i in range(1, N+1):
#1부터 시작할 경우 1을 끝 번호도 추가해줘야 함. 일반적으로 시작이 0이기에 N까지 돌릴때 N번 도는 것!
    if f(i) == True:
        count += 1

print(count)