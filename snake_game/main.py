from turtle import Turtle, Screen

t0 = Turtle(shape="square")
t0.color("white")

t1 = Turtle(shape="square")
t1.color("white")
t1.penup()
t1.goto(-20, 0)




s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")



s.exitonclick()