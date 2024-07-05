from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.relocate()

    def relocate(self):
        new_x = randint(a=-203, b=203)
        new_y = randint(a=-203, b=203)
        self.goto(new_x, new_y)
