import random
import turtle
import turtle as t

def click(x,y):
    print(x,y)
    color = [ "red", "blue", "green", "purple", "brown", "pink", "yellow","magenta", "cyan","olive"]
    myTurtle.pensize(random.randint(1, 5))
    myTurtle.color(random.choice(color))
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    if(random.randint(1, 10)%2==0): #네모
        for _ in range(4):
            myTurtle.right(90)
            myTurtle.forward(100)
    else:    #동그라미
        myTurtle.circle(random.randint(10, 50))

t.title("거북이로 객체지향 사각형그리기")
myTurtle=t.Turtle('turtle')
turtle.onscreenclick(click,1)
t.done()