count = 0
max = 0

for n in range(0, 9):

    count += 1
    number = int(input())

    if max < number:
        max = number
        order = count

print(max, order, sep='\n')
#구분 문자 개행으로 바꿔주기 위한 sep='\n' 활용