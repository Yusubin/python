
# #문제1
# food=[] #ArrayList hobby = new ArrayList();
# food.append(input(""))
# food.append(input())
# food.append(input())
# print(food)
#
#
# for x in food:
#     print(x)
#
#
# for x in food:
#     if(x=="감자"):
#         x="라면"
#     print(x)
#


# #문제2
# month=10
# if(3<month<5):print("봄")
# elif(6<month<8):print("여름")
# elif(9<month<11):print("가을")
# else:print("겨을")
#
# #문제 3
# total=0
# for i in range(10, 20, 1):
#     total=total+i
#
# print(total)



# #문제 4
# target=55
# count=0
# while True:
#     count=count+1
#     answer = int(input("숫자입력"))
#     if target==answer:
#         print("good~")
#         print(str(count)+"번째에 맞춤")
#         break;

# #문제 5
# n1= int(input("시작값 입력"))
# n2= int(input("끝값 입력"))
# count=0
# total=0
# for i in range(n1, n2, 1):
#     count = count+1
#     total = i+total
#
# print("개수:", count, "총합:", total)
#
# #문제 12
# c1=[22, 99, 11, 23]
# c2=[44, 99, 66, 24]
# count= 0
# index = 0
# for i in c1:
#
#     for j in c2:
#        if(i==j):
#            count=count+1
#            print(count)
#            print(index ," ", i)
#     index = index + 1
#

# #


# for i in range(0,3,1):
#     print('*')

#
# #문제1
# num1=int(input("숫자1:"))
# num2=int(input("숫자2:"))
# print(num1+num2,num1-num2,num1*num2,num1/num2)
#
# #문제2
# name=input("입력1(이름):")
# age=int(input("입력2(나이):"))
# print(name, "은", age,"세 입니다.")
# if(age>100):
#     print("나이가 많으시군요")
# else:
#     print("아직 어리시군요.")
#
# #문제 3
# hobby='달리기'
# time=10
# print(hobby, "를", time,"시간 했습니다.")
# if(hobby=="달리기" and time>=10):
#     print("오늘 ", hobby, "는 충분")
# elif(hobby=="달리기" or time<10):
#     print("어떤 운동이든 시작하세요!")
# else: print("어떤 운동이든 시작하세요!")
#
# #1
# buy=[]
# wish=list()
# # #사고싶은것 5개 입력
# for i in range(0,5,1):
#     buy.append(input(""))
# for j in buy:
#   print(j)
#
# #2
# wish = wish + input("입력:").split(',')
# for d in wish:
#     print("나는 "+ d +"가 되고싶어요!")


