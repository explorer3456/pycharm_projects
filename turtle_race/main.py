from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

my_screen.listen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_right():
    my_turtle.right(10)

def turn_left():
    my_turtle.left(10)

def reset_turtle():
    my_turtle.reset()

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=reset_turtle)

my_screen.exitonclick()