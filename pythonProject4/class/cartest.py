class Car:
    color = None
    speed = 0

    def start(self):
        print("차가 출발하다.")

    def stop(self):
        print("차가 멈추다.")

    def __str__(self):
        return str(self.color) + ", " + str(self.speed)


if __name__ == '__main__':
    car1 = Car()
    car1.color="red"
    car1.speed=300
    print(car1)
