# 제어문
# 순차문:입력-->처리-->출력
# 조건문:if, if~else, if~elif....else
# 반복문:while, for
#
#
# num1, num2, ac = input("숫자, 연산자 입력").split()
#
# if(ac=='+'):
#     result=int(num1)+int(num2)
#     print(result)
# elif (ac == '-'):
#     result = int(num1) - int(num2)
#     print(result)
# elif (ac == '/'):
#     result = int(num1) / int(num2)
#     print(result)
# elif (ac == '*'):
#     result = int(num1) * int(num2)
#     print(result)
# else:
#     print("연산자 다시입력")



num1= int(input("숫자1 입력"))
num2= int(input("숫자2 입력"))
ac= input("연산자 입력")

if(ac == '+'):
    result = num1 + num2
    print(result)
elif (ac == '-'):
    result = num1 - num2
    print(result)
elif (ac == '/'):
    result = num1 / num2
    print(result)
elif (ac == '*'):
    result = num1 * num2
    print(result)
else:
    print("연산자 다시입력")