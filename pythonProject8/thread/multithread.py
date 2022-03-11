class RacingCar:
    name = ' '

    def __init__(self, name):
        self.name = name
    def runCar(self):
        for _ in range(3):
            print(self.name, "달립니다")


if __name__ == '__main__':


    car1 = RacingCar("banana")
    car2 = RacingCar("apple")
    car3 = RacingCar("fineapple")


    car1.runCar()
    car2.runCar()
    car3.runCar()

