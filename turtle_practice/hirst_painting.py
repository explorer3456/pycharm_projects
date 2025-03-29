from email.utils import collapse_rfc2231_value
from turtle import Turtle, Screen
import random
import colorgram

color_obj_list = colorgram.extract("image.jpg", 10)

print(type(color_obj_list))
print(type(color_obj_list[0]))

print(color_obj_list)
print(color_obj_list[0])
