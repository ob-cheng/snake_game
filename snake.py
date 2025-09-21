from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_cube = Turtle("square")
            new_cube.color("white")
            new_cube.penup()
            new_cube.goto(position)
            self.segments.append(new_cube)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[2].seth(90)

    def right(self):
        self.segments[2].seth(0)

    def down(self):
        self.segments[2].seth(270)

    def left(self):
        self.segments[2].seth(180)