from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("orange")

def get_random_color():
    R = random.random()
    G = random.random()
    B = random.random()

    return R, G ,B

def draw_line(turtle_obj, shape):
    angle = int(360 / shape)
    turtle_obj.forward(100)
    turtle_obj.right(angle)

for shape_idx in range(3,11):
    R, G, B = get_random_color()
    my_turtle.color(R, G, B)
    for line in range(1, shape_idx+1):
        draw_line(my_turtle, shape_idx)

my_screen = Screen()
my_screen.exitonclick()