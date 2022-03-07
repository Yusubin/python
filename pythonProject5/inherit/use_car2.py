#새로운 클래스를 만들때
#기존의 있던 클래스를 "재사용!"해서
#만드는것을 상속이라고함.

from moving import Car

class Truck(Car):
    #멤버변수 2개, 멤버함수 2개
    weight = 0#멤버변수3개
    def move(self):#멤버함수3개
        print("짐을 싣고 가다. ")