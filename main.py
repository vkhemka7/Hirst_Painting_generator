# import colorgram
#
# colors = colorgram.extract('image.jpeg', 2 ** 32)
# colors_list = []
# for i in range(len(colors)):
#     color_r = colors[i].rgb.r
#     color_g = colors[i].rgb.g
#     color_b = colors[i].rgb.b
#     tuple_color = (color_r, color_g, color_b)
#     colors_list.append(tuple_color)
#
# print(colors_list)
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")
colors = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204), (78, 66, 42), (23, 99, 96)]
timmy.penup()
timmy.setx(-200)
timmy.sety(-200)
timmy.hideturtle()
for j in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    timmy.setx(-200)
    timmy.sety(timmy.ycor() + 50)