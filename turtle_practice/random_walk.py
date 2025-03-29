from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color("orange")
my_turtle.pensize(10)
my_turtle.speed("fastest")

def get_random_color():
    R = random.random()
    G = random.random()
    B = random.random()

    rgb = (R, G, B)
    return rgb

def draw_line(turtle_obj):
    angle = random.randint(1,4);
    turtle_obj.forward(50)

    # change draw type
    turtle_obj.right(angle * 90)

    turtle_obj.color(get_random_color())

while True:
    draw_line(my_turtle)

