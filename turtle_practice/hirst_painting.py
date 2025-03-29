from turtle import Turtle, Screen
import random
import colorgram

data = colorgram.extract("image.jpg", 10)

print(type(data))
print(data)