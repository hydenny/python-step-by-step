N = int(input())

array = list(map(int, input().split()))
#int형으로 list를 선언하며, 띄어쓰기를 통해 그 인덱스를 구분함

max = min = array[0]

for x in range(0, N-1):
    if max < array[x+1]:
        max = array[x+1]
    if min > array[x+1]:
        min = array[x+1]
    """
    if를 하지 않고 else로 진행한 경우 최소값에 대한 조건에 직접 해당하는 것은 아니기 때문에 반례가 존재하는 듯함.
    """

print(min, max)
#출력을 다음과 같이 하면 띄어쓰기로 구분되어 출력이 됨.