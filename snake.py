from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
DISTANCE = 20
DIFF_X = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            self.segments.append(Turtle(shape='square'))
            self.segments[i].penup()
            self.segments[i].color('white')
            self.segments[i].goto(x, 0)
            self.segments[i].speed('fastest')
            x -= DIFF_X

    def move_forward(self):
        for ii in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[ii - 1].xcor()
            new_y = self.segments[ii - 1].ycor()
            self.segments[ii].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self):
        self.segments.append(Turtle(shape='square'))
        self.segments[-1].penup()
        self.segments[-1].color('white')
        x = self.segments[-2].xcor()
        y = self.segments[-2].ycor()
        self.segments[-1].goto(x, y)
        self.segments[-1].speed('fastest')



