S = str(input())

alphabet = []
result = []

for i in range(26):
    alphabet.append(chr(i + 97))
    result.append(-1)
    #알파벳의 아스키 코드값을 활용

for i in range(26):
    if alphabet[i] in S:
        result[i] = S.find(alphabet[i])
        #문자열 중 찾고자 하는 문자가 처음 나오는 위치를 반환해주는 find함수 활용.
        #존재하지 않는 문자라면 -1 반환.

for i in range(len(result)):
    print(str(result[i]), end=' ')