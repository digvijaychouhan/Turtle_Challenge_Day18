import turtle as t
from turtle import Screen
from random import randint, choice

timmy = t.Turtle()
t.colormode(255)

# colors = ["dark slate blue", "green", "red", "blue", "yellow", "brown", "gray", "purple",
# "orange", "royal blue", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# directions = [0, 90, 180, 270]


def random_color():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    my_color = (r, g, b)
    return my_color

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.pensize(2)
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_sides in range(3, 11):
#     timmy.pencolor(choice(colors))
#     draw_shape(shape_sides)


timmy.speed("fastest")
# timmy.pensize(5)

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
