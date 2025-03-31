from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make a bet", prompt="Which color?")
colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
turtle_list =[]

def move_turtles_to_front(t_list):
    num_of_turtle = len(t_list)
    gap = (400/3)/num_of_turtle;

    for i in range(num_of_turtle):
        t_list[i].penup()
        t_list[i].goto(x=-230, y=gap*i)

def is_anyturtle_done(t_list):
    is_done = False
    for t in t_list:
        if t.xcor() >= 230:
            is_done = True
            print(f'turtle {t.color()} has won' )

    return is_done


for i in range(len(colors)):
    t_obj = Turtle(shape="turtle")
    t_obj.color(colors[i])
    turtle_list.append(t_obj)



move_turtles_to_front(turtle_list)

is_race_done = False;

while not is_race_done:
    for t in turtle_list:
        speed = random.randint(0,10);
        t.penup()
        t.forward(speed)

    is_race_done = is_anyturtle_done(turtle_list)

my_screen.exitonclick()