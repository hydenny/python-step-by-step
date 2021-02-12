T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)

    result = ''

    for j in S:
    # for ... in ... 구문에서 사용되는 '집합_변수'는 리스트, 튜플, 문자열 등임.
    # 정수값은 이에 해당하지 않는다.
        j *= R
        result += j

    print(result)