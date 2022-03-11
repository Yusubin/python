import random
import threading

def a1(x,y):
    for i in range (1, 100, 1):
        print("증가>>",i)

def a2(x,y):
    for i in range (x, y+1,-1):
        print("감소>>",i)

def a3(x,y):
    list=["@","#","$","%"]
    for i in range (x,y+1):
        print("특수>>",random.choice(list))

thread1=threading.Thread(target=a1, args=(1,100))
thread2=threading.Thread(target=a2, args=(100,0))
thread3=threading.Thread(target=a3, args=(0,100))
thread1.start()
thread2.start()
thread3.start()

