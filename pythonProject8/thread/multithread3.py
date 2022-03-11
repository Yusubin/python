import random
import threading
import time
import tkinter
from tkinter import *
from tkinter import messagebox


class RacingCar:
    # 멤버변수
    name = ''
    count = 0 #값을 공유할목적으로사용되는 클래스변수
    # 초기화함수
    def __init__(self, name):
        self.name = name

    # 멤버함수
    def runCar(self,carRacing, x1, y1):
        j = 0
        while True:
            j = random.randint(0, 10)
            if x1 >= 1900:
                RacingCar.count+=1
                data = str(RacingCar.count) + "등" + str(self.name)
                messagebox.showinfo("결과>>",data)
                break
            x1 += j
            carRacing.place(x=x1, y=y1)
            time.sleep(0.1)


def run_start():

    print('call ok!!')
    c1 = RacingCar('appleCar')
    c2 = RacingCar('summerCar')
    c3 = RacingCar('springCar')

    t1 = threading.Thread(target=c1.runCar, args= (car_label1, 10, 100))
    t2 = threading.Thread(target=c2.runCar, args= (car_label2, 10, 150))
    t3 = threading.Thread(target=c3.runCar, args= (car_label3, 10, 200))

    t1.start()
    t2.start()
    t3.start()



if __name__ == '__main__':
    window = Tk()
    window.geometry("2000x250")
    window.title('멀티 스레드 자동차 경주')
    b = Button(window, text='멀티 스레드 시작', command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)  # fill x,y축 가득 채우는 것. ipadx 여백
    car1 = tkinter.PhotoImage(file='car1.gif')
    car2 = tkinter.PhotoImage(file='car2.gif')
    car3 = tkinter.PhotoImage(file='car3.gif')
    car_label1 = Label(window, image=car1)
    car_label1.place(x=10, y=100)

    car_label2 = Label(window, image=car2)
    car_label2.place(x=10, y=150)

    car_label3 = Label(window, image=car3)
    car_label3.place(x=10, y=200)

    window.mainloop()
