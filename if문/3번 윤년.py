A = int(input())

if(((A%4 == 0) and (A%100 != 0)) or ((A%4 == 0) and (A%400 == 0))): #그냥 A%4 == 0 and (A%100 != 0 or A%400 == 0)이 더 나은 소스일 듯함
    print("1")
else:
    print("0")