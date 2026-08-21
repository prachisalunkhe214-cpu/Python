'''import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()

turtle.tracer(10)
screen.bgcolor("black")

h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        h += 0.005

        t.right(90)
        t.circle(150 - j * 6, 90)
        t.left(90)
        t.circle(150 - j * 6, 90)
        t.right(180)

    t.circle(40, 24)

turtle.done()'''
'''import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(100):
    t.forward(i * 5)
    t.right(144)

turtle.done()'''
'''import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(36):
    t.circle(100)
    t.right(10)

turtle.done()'''
import turtle

t = turtle.Turtle()
t.speed(5)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(200):
    t.color(colors[i % 6])
    t.forward(i)
    t.right(59)

turtle.done()