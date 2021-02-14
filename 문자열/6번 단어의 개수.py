#문자열 길이가 100만을 넘지 않으면, 최대 길이일 때 for문을 두 번만 돌아도 효율성에 문제가 생길 수 있음.
N = input()

count = 0

if N[0] == ' ':
    if N[-1] == ' ':
        count = N.count(' ') - 1
    else:
        count = N.count(' ')

elif N[-1] == ' ':
    if N[0] == ' ':
        count = N.count(' ') - 1
    else:
        count = N.count(' ')

else:
    count = N.count(' ') + 1

print(count)