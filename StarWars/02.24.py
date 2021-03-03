import turtle
import random
import time

def fel():
    ypozicio=urhajo.ycor()
    ypozicio+=10
    urhajo.sety(ypozicio)


def le():
    ypozicio=urhajo.ycor()
    ypozicio-=10
    urhajo.sety(ypozicio)


def jobbra():
    xpozicio=urhajo.xcor()
    xpozicio+=10
    urhajo.setx(xpozicio)


def balra():
    xpozicio=urhajo.xcor()
    xpozicio-=10
    urhajo.setx(xpozicio)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("Background.png")
space.addshape("sprite.gif")
space.addshape("meteor1.gif")

space.tracer(0)
space.listen()
space.onkey(fel, "Up")
space.onkey(le, "Down")
space.onkey(jobbra, "Right")
space.onkey(balra, "Left")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor1 = turtle.Turtle()
meteor1.shape("meteor1.gif")
meteor1.penup()

while True:
    space.update()
    time.sleep(0.2)

    if urhajo.ycor() > 300:
        urhajo.sety(-300)

    if urhajo.xcor() > 400:
        urhajo.setx(-400)

    if urhajo.ycor() < -300:
        urhajo.sety(300)

    if urhajo.xcor() < -400:
        urhajo.setx(400)

    if urhajo.distance(meteor1.xcor(), meteor1.ycor()) < 15:
        x = random.randint(-380, 380)
        y = random.randint(-280, 280) 
        meteor1.goto(x, y)