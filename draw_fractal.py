import turtle

def draw_triang(some_turtle):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    brad.left(75)
    for i in range(1,10):
        draw_triang(brad)
        brad.forward(50)
        window.bgcolor("blue")

    window.bgcolor("black")

    window.exitonclick()

draw_art()
               
