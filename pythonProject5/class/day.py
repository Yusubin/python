class Day:
    work = None
    hour = 0
    place = None
    count = 0
    time_total=0
    def __init__(self, work, hour, place):
        self.place=place
        self.work=work
        self.hour=hour

        #이니셜라이저가 호출될때마다 몇개의 객체가 생성되었는지 프린트
        Day.count += 1
        Day.time_total += self.hour

    def __str__(self) :
        # return str(self.hour)+","+str(self.work)+","+str(self.place)
        return str(self.hour)+","+str(self.work)+","+str(self.place)


