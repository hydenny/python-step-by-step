word = input()

alphabet = []
counting = []
upper = []

alphabet = set(word.upper())
#대문자로 전부 바꿔주는 upper().
#소문자로 바꾸려면 lower()을 쓰면 됨.

if len(word) == 1:
    print(word.upper())
    quit()

else:
    count = 0

    upper = word.upper()

    for i in alphabet:
        for j in upper:
            if i == j:
                count += 1
        counting.append([i, count])
        count = 0

    counting.sort(key=lambda x: x[1], reverse=True)
    #sorted 메소드는 리스트를 직접 수정하지 않으므로 sort를 잘 쓰는 것이 훨씬 유용함

    if counting[0][1] == counting[1][1]:
        print('?')
    else:
        print(counting[0][0])