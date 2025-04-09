import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("America States")
image = "blank_states_img.gif"

# how to add picture as background
screen.addshape(image)
turtle.shape(image)


us_data = pandas.read_csv("50_states.csv")

user_x = 0
user_y = 0
is_game_done = False
count = 0

print(type(us_data.state))

state_data = us_data[us_data.state == "Texas"]
print(state_data)
print(type(state_data))
print(state_data.state == "Texas")


while not is_game_done:
    user_answer = turtle.textinput(title=f'enter state name{count}/50', prompt="enter state name ?").lower()

    state_data = us_data[us_data.state.str.lower() == user_answer]

    if not state_data.empty:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(arg=state_data.state.item(), align="center")


turtle.mainloop()

# screen.exitonclick()