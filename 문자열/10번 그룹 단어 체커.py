N = int(input())

count = 0

for _ in range(N):
    word = input()
    word_list = list(word)

    change = 0
    change_list = 0

    for i in range(len(word)-1):
        if word_list[i] != word_list[i+1]:
            change += 1

    word_list.sort()

    for i in range(len(word_list)-1):
        if word_list[i] != word_list[i+1]:
            change_list += 1

    if change == change_list:
        count += 1

print(count)