#데이터 입력
from builtins import print

name = input('이름을 입력>')#Ctrl+alt+화살표아래
age = input('나이를 입력')

#처리
print(type(age))#모든입력은 str
age2 = int(age)+1
#출력
print('당신이 입력한 이름은'+ name)
print('당신이 입력한 나이는'+ age)
print('당신의 내년 나이는'+ str(age2))