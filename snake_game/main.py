from turtle import Turtle, Screen
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

t_list = []
is_game_done = False

for i in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t_list.append(t)

while not is_game_done:
    for i in range(len(t_list)-1, -1, -1):
        t_list[i].penup()

        if i > 0:
            t_list[i].goto(t_list[i-1].xcor(), t_list[i-1].ycor())
    t_list[0].forward(20)
    t_list[0].left(90)
    time.sleep(1)
    s.update()

s.exitonclick()