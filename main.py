import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []

starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    new_cube = Turtle("square")
    new_cube.color("white")
    new_cube.penup()
    new_cube.goto(position)
    segments.append(new_cube)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()