A, B, C = input().split()
A = int(A)  #나머지 연산자는 정수에 사용한다.
B = int(B)
C = int(C)
print((A+B) % C)
print(((A % C)+(B % C)) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)