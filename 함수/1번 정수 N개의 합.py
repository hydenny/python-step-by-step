def solve(a):
#함수 선언시 def func(): 와 같은 형식으로 선언하며, 함수에 쓸 파라미터를 괄호 안에 제시함
#ex) def function(a):

    ans = 0

    for i in a:
        ans = ans + i

    return ans
