# import turtle
# tim1 = turtle.Turtle()
# tim1.color("blue")
# screen = turtle.Screen()

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# tim.shape("turtle")
# tim.color("blue")
# tim.pencolor("#33cc8c")

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# import turtle as t
# tim1 = t.Turtle()
# screen = t.Screen()


# import heroes
# print(heroes.gen())

# for i in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# def drawShape(side):
#     angle = 360/side
#     for _ in range(side):
#         tim.pendown()
#         tim.forward(100)
#         tim.right(angle)
#
#
# for i in range(3, 12):
#     drawShape(i)
#
# screen.exitonclick()

# import turtle as t
# import random
# screen = t.Screen()
# t.colormode(255)
# tim = t.Turtle()
# tim.pensize(15)
# tim.speed("fastest")
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_colo = (r,g,b)
#     return random_colo
#
# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen.exitonclick()

# import turtle as t
# import random
# screen = t.Screen()
# tim = t.Turtle()
# tim.speed("fastest")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_colo = (r,g,b)
#     return random_colo
#
#
# def drawSpirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         current_heading = tim.heading()
#         tim.setheading(current_heading+size_of_gap)
#
#
# drawSpirograph(5)
# screen.exitonclick()
import random


import colorgram

rgb_colors = []

colors = colorgram.extract('imgae.jpeg', 30)

for color in colors:
    re = color.rgb.r
    gr = color.rgb.g
    bl = color.rgb.b
    rgb_colors.append((re, gr, bl))

import turtle as t
import random

t.colormode(255)
screen = t.Screen()
tim = t.Turtle()
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
