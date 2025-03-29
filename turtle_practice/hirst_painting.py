from email.utils import collapse_rfc2231_value
from turtle import Turtle, Screen
import random
import colorgram

my_turtle = Turtle()
my_turtle.shape("circle")
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

for x in range(-400,0,40):
    for y in range(-400,0,40):
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()
        my_turtle.stamp()
        my_turtle.color(get_random_color())

my_screen.exitonclick()