# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
# def move_downwards():
#     tim.back(10)
# def move_left():
#     ch = tim.heading() + 10
#     tim.setheading(ch)
# def move_right():
#     ch = tim.heading() - 10
#     tim.setheading(ch)
#
# def clearsc():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key='w',fun=move_forwards)
# screen.onkey(key='s',fun=move_downwards)
# screen.onkey(key='a',fun=move_left)
# screen.onkey(key='d',fun=move_right)
# screen.onkey(key = 'c',fun=clearsc)
# screen.exitonclick()

import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color : ")
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'blue']
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if(winning_color == user_bet):
                print(f"Yay!. You guessed right!. The {winning_color} is the winner")
            else:
                print(f"Nope, {winning_color} is the winner ")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()