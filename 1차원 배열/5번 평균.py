N = int(input())

score = list(map(int, input().split()))

score.sort()
score.reverse()
#reverse()는 단순히 리시트의 순서를 뒤집는거고, sort(reverse=True)는 내림차순으로 정렬하는 것.

M = score[0]

for i in range(0, len(score)):
    score[i] = score[i]/M*100

sum = 0
average = 0

for i in range(0, len(score)):
    sum = sum + score[i]

average = sum/len(score)

print(average)