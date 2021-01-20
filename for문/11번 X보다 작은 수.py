N, X = input().split()
N = int(N)
X = int(X)

A = list(map(int, input().split()))
#리스트 생성해주고 입력 받은 수를 나누어 저장하기 위해 list(map(int, input().split()))로 작성함.
for i in range(0, N):
        if A[i] < X:
            print(A[i], end=" ")
            #print시에 end옵션을 " "한 칸 띄어주는 공백으로 줌