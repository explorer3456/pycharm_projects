import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUM_OF_CAR = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

car_list =[]

for _ in range(NUM_OF_CAR):
    car_list.append(CarManager())


def is_turtle_hit_car(t_obj, c_obj):
    return t_obj.distance(c_obj) < 15 and (t_obj.ycor() - c_obj.ycor() < 5)

screen.onkey(fun=player.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for c in car_list:
        c.move()

    for c in car_list:
        if is_turtle_hit_car(player, c):
            print(f'hit')

screen.exitonclick()

