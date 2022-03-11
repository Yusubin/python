import random
import threading
import time
import tkinter
from tkinter import *


class RacingCar:
    name = ' '
    img = ' '

    def __init__(self, name, img):
        self.name = name
        self.img = img
        image = Label(w, image=img)
        image.pack()

    def runCar(self,carRacing, x1,y1):
        j=0
        while True:
            j=random.radint(0,10)
            if x1 >=400:
                break
            carRacing.place(x=x1+j, y=y1)
            time.sleep(0.5)
        for _ in range(10):
            print(self.name, "달립니다")


# car1 = RacingCar("banana")
# car2 = RacingCar("apple")
# car3 = RacingCar("fineapple")
#
# t1 = threading.Thread(target=car1.runCar)
# t2 = threading.Thread(target=car2.runCar)
# t3 = threading.Thread(target=car3.runCar)
#
# t1.start()
# t2.start()
# t3.start()



def start():
    c1 = RacingCar("apple")
    c2 = RacingCar("banana")
    c3 = RacingCar("pineapple")


if __name__ == '__main__':
    w = Tk()
    w.geometry("500x200")
    start1 = Button(w, text='경주 시작', font=('고딕', 10), bg='yellow', command=start)
    start1.pack(side=TOP, fill=X, ipadx=10, ipady=10)
    car1 = tkinter.PhotoImage(file='car1.gif')
    car2 = tkinter.PhotoImage(file='car2.gif')
    car3 = tkinter.PhotoImage(file='car3.gif')
    c1 = RacingCar("apple")
    c2 = RacingCar("banana")
    c3 = RacingCar("pineapple")

    car_label1 = Label(w, image=car1)
    car_label1.place(x=10, y=50)

    car_label2 = Label(w,image=car2)
    car_label2.place(x=10, y=100)

    car_label3 = Label(w, image=car3)
    car_label3.place(x=10, y=150)



    w.mainloop()
