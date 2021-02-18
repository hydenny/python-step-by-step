N = int(input())

count = 0

for _ in range(N):
    word = input()
    to_find = []
    number = 0
    find_it = ''

    to_find = list(word)

    for i in range(len(to_find)-1):
        find_it = to_find[i]
        if to_find[i] == to_find[i+1]:
            number += 1

    if number != to_find.count(find_it):
        continue
    else:
        count += 1

print(count)