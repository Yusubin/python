
def add(a,b): #a,b=>매개변수(파라메터)
    return a+b

#함수의 이름을 하나로 동일하게 쓸수업삳.
#다형성(오버로딩)을 지원하지않음
#default로 설정하고싶으면 파라메터 위치를 뒤에서부터 써주어야한다. ]
# 앞의 파라메터는 입력해주고 입력해주지않은 뒤의 파라메터를 default값으로 입력해주라고 처리되기때문
def minus(a,b=100):
    return a - b

def mul(a,b):

    return a * b

def div(a,b):
    return a / b