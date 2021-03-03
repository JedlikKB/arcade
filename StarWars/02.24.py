import turtle
import random
import time

def fel():
    ypozizcio= urhajo.ycor()
    ypozizcio += 10
    urhajo.sety(ypozizcio)


def le():
    ypozizcio= urhajo.ycor()
    ypozizcio -= 10
    urhajo.sety(ypozizcio)


def jobbra():
    xpozizcio= urhajo.xcor()
    xpozizcio += 10
    urhajo.setx(xpozizcio)


def balra():
    xpozizcio= urhajo.xcor()
    xpozizcio -= 10
    urhajo.setx(xpozizcio)

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("background.png")
space.addshape("sprite.gif")
space.tracer(0)
space.listen()
space.onkey(balra,"Left")
space.onkey(jobbra,"Right")
space.onkey(fel,"Up")
space.onkey(le,"Down")


urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

while True:

    space.update()
    time.sleep(0.2)

    if urhajo.ycor()>300:
        urhajo.sety(-300)
    if urhajo.xcor()>400:
        urhajo.setx(-400)
    if urhajo.xcor()<-400:
        urhajo.setx(400)
    if urhajo.ycor()<-300:
        urhajo.sety(300)


