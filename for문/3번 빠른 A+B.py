import sys  #sys.stdin.readline을 쓰기 위한 sys 모듈 import
input = sys.stdin.readline  #단순한 input 대신 sys.stdin.readline을 사용하면 입출력 방식을 빠르게 할 수 있음.

T = int(input())    #sys.stdin.readline에서도 int형으로 변환하는 과정이 가능함.

for T in range(0, T):
    A, B = input().rstrip().split() #맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 써줘야 함.
    A = int(A)
    B = int(B)
    print(A+B)