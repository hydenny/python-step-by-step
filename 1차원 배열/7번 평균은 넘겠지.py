C = int(input())

for i in range(0, C):
    array = list(map(int, input().split()))

    count = 0

    for j in array:
        average = sum(array[1:])/array[0]
        #리스트에서 인덱스 표기법으로 구분지어 사용하면 그 쓰임이 훨씬 유용함.

    for k in array[1:]:
        if k > average:
            count += 1

    print('%.3f'%(count/array[0]*100) + '%')
    #연산 값을 소수 3째자리로 제한해 표현하기 위한 방법
    #'%.nf' % (소수자리수로 나타낼 수)