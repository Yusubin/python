print('1.여기가 시작입니다')

# result =3/0 #ZeroDivisionError >> 이아래로는 실행이 멈춰버림

try:
    result =3/0
    print(result)

#에러의 종류에 따라 다르게 처리할수있음.
except ZeroDivisionError:
    result = 0
    print(result)
except IndexError:
    print("예외처리하였음")



print('2.여기가 중간입니다')
print('3.여기가 끝입니다')