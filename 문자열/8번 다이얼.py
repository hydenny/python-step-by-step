word = input()

change = []

for i in range(len(word)):
    if word[i] in ('A', 'B', 'C'):
        change.append(3)
    elif word[i] in ('D', 'E', 'F'):
        change.append(4)
    elif word[i] in ('G', 'H', 'I'):
        change.append(5)
    elif word[i] in ('J', 'K', 'L'):
        change.append(6)
    elif word[i] in ('M', 'N', 'O'):
        change.append(7)
    elif word[i] in ('P', 'Q', 'R', 'S'):
        change.append(8)
    elif word[i] in ('T', 'U', 'V'):
        change.append(9)
    elif word[i] in ('W', 'X', 'Y', 'Z'):
        change.append(10)
    else:
        change.append(11)
#처음에 if word[i] == 'A' or 'B' o 'C'로 했는데 이는 word[i]에 대해 나머지들을 비교하는 연산이 아니기 때문에 오류가 남.
#부울 식이 작동하는 방식을 제대로 알고 있어야 함.

time = 0

for i in change:
    time += i

print(time)