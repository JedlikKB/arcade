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
space.addshape("meteor2.gif")
space.tracer(0)
space.listen()
space.onkeypress(balra,"Left")
space.onkeypress(jobbra,"Right")
space.onkeypress(fel,"Up")
space.onkeypress(le,"Down")


urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor_jobb = turtle.Turtle()
meteor_jobb.shape("meteor2.gif")
meteor_jobb.penup()

meteor_jobb.setx(400)
while meteor_jobb.xcor()>-400:
    space.update()
    time.sleep(0.1)
    meteor_mozgas = meteor_jobb.xcor()
    meteor_mozgas -= 10
    meteor_jobb.setx(meteor_mozgas)

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