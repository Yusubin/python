from day import Day
if __name__ == '__main__':

    #객체가 생성될때마다 이니셜라이저함수가 자동호출
    #멤버변수가 복사된다.

    day1=Day("자바공부", 1, "강남")
    print(Day.count)
    day2=Day("여행", 15, "강원도")
    print(Day.count)
    day3=Day("운동", 11, "피트니스")
    print(Day.time_total)
    print("평균 하는일의 시간은: ", (Day.time_total/Day.count))
    # print("전체 하는일의 시간은: ", (day1.hour+day2.hour+ day3.hour))
    print("전체 하는일의 시간은: ", Day.time_total)
    print("매일 무엇을 얼마나 어디에서 했는지 프린트", day1, day2, day3)
    print("며칠간 했는지?: ", (Day.time_total/24))