class Phone:

    def text(self):
        print("문자를 보냄")
    def call(self):
        print("전화통화를 하다")


class SamsungPhone(Phone):
    name=None

    # def __init__(self, name):
    #     self.name=name
    def game(self):
        print(self.name, "과 게임을 하다")
    def internet(self,time):
        print(str(time)+ "시간 인터넷하다")


class ApplePhone(Phone):
    size = 0

    def picture(self):
        print("사진을 찍다")

    def youtube(self, time, subject):
        print(str(time)+"시간 동안"+str(subject)+"라는 주제로 유튜브하다.")