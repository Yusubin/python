class Shop:
    genre = None  # 가게종류
    location = None  # 위치

    def total_price(self, num, price):
        r_price = num * price
        print("총 결제금액은" + str(r_price) + "입니다.")

    def total_count(self, today, a=100):
        visit = today-a
        print("오늘은 평균보다" + str(visit) + "명 많이 들어왔어요")



    def __str__(self):
        return str(self.genre) + ", " + str(self.location)

