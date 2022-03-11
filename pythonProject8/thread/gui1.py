import random
import turtle as t

t1 = t.Pen();
while True:
    answer =int(input("선택: 1) 네모    2) 별"))
    t1.penup()
    # x = random.randint(-500, 500)
    # y = random.randint(-500, 500)
    x = t1.xcor()
    y = t1.ycor()
    color=["red", "blue","green","purple","brown","pink","yellow"]
    t1.pensize(random.randint(1,5))
    t1.color(random.choice(color))
    t1.setpos(x,y)
    t1.pendown()
    if answer == 1:
        for _ in range(4):
            t1.right(90)
            t1.forward(100)
    if answer == 2 :
        for _ in range(20):
            t1.right(110)
            t1.forward(100)
    #
    # distance= int(input("얼마나 이동할건지"))
    # direction = int(input("각도입력"))
    # direction2 = input("오른쪽(right)/왼쪽(left)")
    # if direction2 =="left":
    #     t1.left(direction)
    #     t1.forward(distance)
    # if direction2 =="right":
    #     t1.right(direction)
    #     t1.forward(distance)