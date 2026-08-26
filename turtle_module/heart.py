import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["cyan", "blue", "purple", "magenta"]

for i in range(120):
    t.color(colors[i % 4])
    t.forward(i * 2)
    t.right(121)

turtle.done()