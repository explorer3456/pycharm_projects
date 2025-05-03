from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color("orange")
my_turtle.pensize(1)
my_turtle.speed("fastest")

def get_random_color():
    R = random.random()
    G = random.random()
    B = random.random()

    rgb = (R, G, B)
    return rgb

def draw_line(turtle_obj, num_of_loop):
    turtle_obj.circle(100)

    # change draw type
    # turtle_obj.setheading( turtle_obj.heading() + 360/num_of_loop)
    turtle_obj.right(360/num_of_loop)
    turtle_obj.color(get_random_color())


for _ in range(100):
    draw_line(my_turtle, 100)


my_screen = Screen()
my_screen.exitonclick()