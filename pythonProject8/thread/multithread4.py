import random
import threading
import time
import tkinter
from tkinter import *
from tkinter import messagebox


class RacingCar:
    # 멤버변수
    name = None
    count = 0  # 값을 공유할목적으로사용되는 클래스변수
    car_label =None
    # 초기화함수
    def __init__(self, name, img,x1, y1):
        self.name = name
        self.car_label = Label(window, image=img)
        self.car_label.place(x=x1, y=y1)
        thread = threading.Thread(target=self.runCar, args=(x1, y1))
        thread.start()
    # 멤버함수
    def runCar(self, x1, y1):
        j = 0
        while True:
            j = random.randint(0, 10)
            if x1 >= 1900:
                RacingCar.count += 1
                if RacingCar.count >9:
                    RacingCar.count=1
                data = str(RacingCar.count) + "등" + str(self.name)
                messagebox.showinfo("결과>>", data)
                break
            x1 += j
            self.car_label.place(x=x1, y=y1)
            time.sleep(0.1)


def run_start():
    list=[car1, car2, car3]
    for i in range(9):
        RacingCar('car'+str(i), random.choice(list), 10, 100+i*50)




if __name__ == '__main__':
    window = Tk()
    window.geometry("2000x600")
    window.title('멀티 스레드 자동차 경주')

    car1 = tkinter.PhotoImage(file='car1.gif')
    car2 = tkinter.PhotoImage(file='car2.gif')
    car3 = tkinter.PhotoImage(file='car3.gif')

    b = Button(window, text='멀티 스레드 시작', command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)  # fill x,y축 가득 채우는 것. ipadx 여백

    window.mainloop()
