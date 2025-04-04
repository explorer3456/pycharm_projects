from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score



s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)
s.listen()


food = Food()

score = Score()

snake = Snake()

s.onkey(fun=snake.up, key="w")
s.onkey(fun=snake.down, key="s")
s.onkey(fun=snake.left, key="a")
s.onkey(fun=snake.right, key="d")


is_game_done = False

def is_collision_with_wall(snake_obj):
    x = snake_obj.body_list[0].xcor()
    y = snake_obj.body_list[0].ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        return True
    else:
        return False


while not is_game_done:
    s.update()
    snake.move()
    time.sleep(0.1)

    if snake.body_list[0].distance(food) < 17:
        food.refresh()
        score.update_score()
        score.display_score()
    if is_collision_with_wall(snake):
        is_game_done = True
        score.show_game_over()






s.exitonclick()
