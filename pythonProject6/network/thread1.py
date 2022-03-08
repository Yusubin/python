import threading

def a1(x,y):
    for i in range (x, y+1):
        print("a1번>>",i)


def a2(x,y):
    for i in range (x, y+1):
        print("a2번>>",i)


def a3(x,y):
    for i in range (x, y+1):
        print("a3번>>",i)


thread1=threading.Thread(target=a1, args=(1,100))
thread2=threading.Thread(target=a2, args=(0,50))
thread3=threading.Thread(target=a3, args=(5,120))
thread1.start()
thread2.start()
thread3.start()