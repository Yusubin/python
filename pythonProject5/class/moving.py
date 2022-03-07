class Car:  # 대문자를 쓰는게 클래스를 구분하기 편하다.
    # 멤버변수
    color = None
    shape = None

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    # 멤버함수
    def speed_up(self):
        print(self.color + '속도를 UP')

    def speed_down(self):
        print('자동차의 속도를 DOWN')

    def __str__(self):
        return str(self.color) + "," + str(self.shape)


class Bike:
    color = None
    model = None
    speed = 0
    
    #생성자, 멤버 변수 초기화 해주는 것 ..... initializer
    #객체 생성시 자동호출
    def __init__(self, color, model, speed):
        self.color = color
        self.speed = speed
        self.model = model

    def __str__(self):
        return str(self.color) + "," + str(self.model) + "," + str(self.speed)

    def wear_protective_gear(self):
        print("보호 장비 착용")

    def speed_up(self):
        self.speed += 1
        return self.speed

    def change_color(self,c):
        self.color=c
        return c