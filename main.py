import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("orange")

for _ in range(50):
    my_turtle.forward(10)
    if my_turtle.isdown():
        my_turtle.penup()
    else:
        my_turtle.pendown()


my_screen = Screen()
my_screen.exitonclick()