A, B = input().split()
"""
두 수를 한번에 입력받을 경우 string으로 받아지므로
한 번에 int로 받지 말고 따로 나눠서 형변환 해줌
"""
A = int(A)
B = int(B)

if(A > B):  #파이썬의 if문에서는 :를 붙여줌
    print(">")
elif(A < B):
    print("<")
else:
    print("==")