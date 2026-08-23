import turtle
import colorsys

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Art")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Start position
t.penup()
t.goto(0, 0)
t.pendown()

# Color value
h = 0

# Draw pattern
for i in range(150):

    # Generate HSV color
    color = colorsys.hsv_to_rgb(
        h,
        1,
        1
    )

    # Convert RGB values to Turtle color
    t.pencolor(color)

    # Draw
    t.forward(i * 2.8)
    t.right(165)

    # Change color
    h += 0.005

# Keep window open
turtle.done()