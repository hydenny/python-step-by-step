while True:
#while문을 항상 참으로 하는 True
    try:
    #A,B가 구분되어 주어진 상황일 경우에만 입력받아 수행하는 문구
        A, B = map(int, input().split())
        print(str(A + B))
    except:
    #try에 대한 에러가 발생한 경우(여기서는 입력이 주어지지 않은 경우)
        break