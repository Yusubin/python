# import object.moving
from moving import *
if __name__ == '__main__':
    car1 = Car("세모", "red")

    #
    # car2 = Car()
    # car2.color = "blue"
    # car2.shape = "네모"
    #
    # car2.speed_up()

    b1=Bike("blue", "carnival" , 25)
    # b1.color = "blue"
    # b1.speed = 24
    # b1.model = "carnival"

    print(b1)
    b1.wear_protective_gear()
    print(b1.speed_up())
