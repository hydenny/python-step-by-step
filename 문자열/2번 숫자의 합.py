N = int(input())

string = str(input())
#문자열로 받아서 수행해야 하므로 str으로 받고 나중에 int로 형변환을 하며 연산해줌

sum = 0

for i in string:
    sum += int(i)

print(sum)