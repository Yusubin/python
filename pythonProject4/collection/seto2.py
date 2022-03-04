#얕은복사 깊은복사

#기본형 
# 복사: 정수실수문자열  // 변수의 값이들어있기때문에.......
x=100
y=x
print(x,y)
y=200
print(x,y)

# 참조형 변수는 복사할때 = 사용하지않고 함수 써야함.....
# 얕은복사!!! 대입연산자 ==변수의 주소값을 복사해
jumsu_1 = [10, 20, 30]
# jumsu_2 = jumsu_1 #얕은복사
jumsu_2=jumsu_1.copy() #깊은복사...Java에서는 clone
jumsu_2[0] = 99
print(jumsu_2)
print(jumsu_1)
jumsu_2[1] = 5

print(jumsu_2)
print(jumsu_1)