def d(n):
    sum = n

    while n > 0:
        sum = sum + n%10
        n = int(n/10)

    return sum

list = [0]

list = list * 10000

i = 1

while i < 10000:
    list[d(i)-1] = 1
    i += 1

j = 0

for j in range(len(list)):
    if list[j] == 0:
        print(j+1)