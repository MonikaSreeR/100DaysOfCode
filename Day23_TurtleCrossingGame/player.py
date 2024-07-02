from turtle import Turtle
START_POSITION = (0,-280)
DISTANCE=10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(DISTANCE)

    def start_position(self):
        self.goto(START_POSITION)