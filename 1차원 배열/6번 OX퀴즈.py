N = int(input())

for i in range(0, N):
    result = list(map(str, input()))
    #문자 혹은 문자열 단위로 인덱스에 리스트를 구성하려면 str을 씀.

    total = 0
    score = 0

    for j in range(0, len(result)):

        if j+1 < len(result):
            if result[j] == 'O':
                score = score + 1
            else:
                score = 0

        else:
            if result[j] == 'O':
                score = score + 1
            else:
                score = 0

        #print(score)
        total = total + score

    print(total)