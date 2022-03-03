#
# #문제1
# food=[] #ArrayList hobby = new ArrayList();
# for _ in range(3):
#     food.append(input())
#
# print(food[1])
# print(food[0:2])
# print(food[1:])
# # food[0]='라면'
# for x in food:
#     if(x=="감자"):
#         x="라면"
#     print(x, end=" ")
#
#
# #
# # #문제2
# import datetime
# today=datetime.datetime.today()
# if(3 <=today.month<=5):print("봄")
# elif(6<=today.month<=8):print("여름")
# elif(9<=today.month<=11):print("가을")
# else:print("겨을")
# #
# # #문제 3
# total=0
# for i in range(10, 20, 1):
#     total=total+i
#
# print(total)
#
# #
# #
# # # 문제 4
# import random
# target = random.randint(1,100)
# count = 0
# while True:
#     count = count + 1
#     answer = int(input("숫자입력"))
#     if target == answer:
#         print("good~")
#         print(str(count) + "번째에 맞춤")
#         break;
#     elif target > answer:
#         print("너무적음")
#     else:
#         print("너무 큼")
#
# # #문제 5
# n1= int(input("시작값 입력"))
# n2= int(input("끝값 입력"))
# count=len(list(range(n1, n2+1)))
# count=0
# total=0
# for i in range(n1, n2, 1):
#     count = count+1
#     total = i+total
#
# aver=total/count
# print("개수:", count, "총합:", total, "평균:", aver)

#1ckdnjs 0번부터 9번까지 좌석이잇음
# 예매를 원하는 좌석을 한번에 한자리씩예매
#예매한 자리 가격 출력, 위치 출력.
# seat=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# count_seat=[]
# print(seat)
# print("종료하려면 종료 입력")
# print("------------------------------------------")
# while True:
#     ticket=input("원하는 좌석 입력 >")
#
#     if ticket == "종료":#종료조건
#         print(seat)
#         break
#
#     for i in seat:
#         if int(ticket) == i:
#             count_seat.append(i);
#             seat[i]="sold out"
#             print("남은자리:", seat)
#             print("------------------------------------------")
#
# print("------------------------------------------")
# print("예매한 좌석:", count_seat, "총", len(count_seat),"자리 예매완료")
# print("가격:", len(count_seat)*11000)

for i in range(0,10):
    print(i, end="  ")

print()
seat=[0]*10
count_seat=[]
print(seat)
print("종료하려면 -1 입력")
print("------------------------------------------")
while True:
    ticket=int(input("원하는 좌석 입력 >"))

    if ticket == -1:#종료조건
        print(seat)
        break

    if seat[ticket] == 0:
        count_seat.append(ticket);
        seat[ticket]=1
        print("남은자리:", seat)
        print("------------------------------------------")
    else:
        print("이미 예매된 자리.")


print("------------------------------------------")
print("예매한 좌석:", count_seat, "총", len(count_seat),"자리 예매완료")
print("가격:", len(count_seat)*11000)
# #
