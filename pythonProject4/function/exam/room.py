class Tv:
    color = None #tv색상
    ch = 0 #채널
    tel = None  # tv통신사

    def on(self):
        print("___ON___")

    def off(self):
        print("___OFF___")

    def channel(self,ch1):
        print(str(ch1)+"로 채널변경")

    def __str__(self):
        return str(self.color) + ", " + str(self.ch)+ ", " + str(self.tel)

