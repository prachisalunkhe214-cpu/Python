import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(200):
    t.color(colors[i % 6])
    t.forward(i)
    t.right(59)

turtle.done()