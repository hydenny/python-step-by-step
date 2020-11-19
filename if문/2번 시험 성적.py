score = int(input())

if(90<=score<=100): #파이썬에서는 a<b<c꼴로 한번에 비교표현이 가능함
    print("A")
elif(80<=score<=89):
    print("B")
elif(70<=score<=79):
    print("C")
elif(60<=score<=69):
    print("D")
else:
    print("F")