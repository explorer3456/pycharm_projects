from email.utils import collapse_rfc2231_value
from turtle import Turtle, Screen
import random
import colorgram

my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color("orange")
my_turtle.pensize(10)
my_turtle.speed("fastest")

my_screen = Screen()
my_screen.colormode(255)

color_obj_list = colorgram.extract("image.jpg", 10)

hirst_color_list = []

for c in color_obj_list:
    hirst_color_list.append(c.rgb)

def get_random_color():

    rgb_list = random.choice(hirst_color_list)

    return rgb_list

def draw_line(turtle_obj):
    angle = random.randint(1,4);
    turtle_obj.forward(50)

    # change draw type
    turtle_obj.right(angle * 90)

    turtle_obj.color(get_random_color())

while True:
    draw_line(my_turtle)

my_screen.exitonclick()