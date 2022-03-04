print("-------------콘도예약을 진행합니다--------------")
print("원하는 지역을 신청해주세요 (각 지역은 2명까지 신청가능)")
print("1)강원도 2)전라도 3)파주 4)제주도 5)충청도")
print("--------------------------------------------")

area_list = [0, 1, 0, 0, 0]
print(area_list)

while True:

    answer = int(input("원하시는 지역코드를 입력하세요(종료를 원하면 0)"))
    if (answer == 0):
        break

    if area_list[answer] < 2:
        area_list[answer] += 1
        print("신청이가능합니다. 신청완료")
    else:
        print("신청이불가능합니다.")
