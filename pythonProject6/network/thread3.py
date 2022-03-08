import random
import datetime
import threading

#현재시각을 찍는
import time


def cal_show():
    for i in range(100):
        time.sleep(1)
        print(datetime.datetime.now())

def wish_food():
    list=["간장게장","해물탕","꼬막","전복파스타","양념게장","해물찜","아구찜","김치찌개","계란말이"]
    for i in range(0,9,1):
        time.sleep(10)
        print(list[i])

def count(x,y):
    count=0
    for i in range(x,y+2,1):
        time.sleep(1)
        print(count)
        count += 1




th1 = threading.Thread(target=cal_show)
th2 = threading.Thread(target=wish_food)
th3 = threading.Thread(target=count, args=(1,500))
th1.start()
th2.start()
th3.start()
