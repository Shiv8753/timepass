import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_shiva():
    # Draw face
    draw_circle("blue", 100, 0, -100)

    # Draw eyes
    draw_circle("white", 15, -35, -50)
    draw_circle("white", 15, 35, -50)
    draw_circle("black", 5, -35, -50)
    draw_circle("black", 5, 35, -50)

    # Draw mouth
    turtle.penup()
    turtle.goto(-30, -80)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30, 180)

    # Draw hair
    turtle.penup()
    turtle.goto(-120, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(120, 0)
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
    turtle.goto(-120, 0)
    turtle.end_fill()

    # Draw trident
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("gray")
    turtle.goto(0, 100)
    turtle.goto(-10, 90)
    turtle.goto(0, 100)
    turtle.goto(10, 90)
    turtle.goto(0, 100)

    # Draw the third eye
    draw_circle("red", 10, 0, 20)

    # Draw the crescent moon
    draw_circle("white", 20, -40, 80)

    # Draw the snake around the neck
    turtle.penup()
    turtle.goto(-60, -30)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(60, 180)
    turtle.goto(-60, -30)
    turtle.end_fill()

# Set up the turtle environment
turtle.speed(3)
turtle.bgcolor("lightblue")

# Draw Lord Shiva
draw_shiva()

# Finish
turtle.hideturtle()
turtle.done()