import random
import turtle
import turtle as t
def nemo():
    for _ in range(4):
        myTurtle.right(90)
        myTurtle.forward(100)

def circle():
    myTurtle.circle(10)
def click(x,y):
    print(x,y)
    color = [ "red", "blue", "green", "purple", "brown", "pink", "yellow"]
    myTurtle.pensize(random.randint(1, 5))
    myTurtle.color(random.choice(color))
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    if(x > 0):nemo()
    else: circle()


t.title("거북이로 객체지향 사각형그리기")
myTurtle=t.Turtle('turtle')


turtle.onscreenclick(click,1)
t.done()