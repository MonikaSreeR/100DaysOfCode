from turtle import Turtle
from random import randint, choice

class Block(Turtle):
    def __init__(self):
        self.blocks = []

    def create_block(self):
        if choice([True, False]):
            new_block = Turtle()
            random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            new_block.color(random_color)
            new_block.shape("square")
            new_block.shapesize(stretch_wid=0.5, stretch_len=2)
            new_block.penup()
            new_block.goto(380, randint(-240, 260))
            new_block.setheading(180)
            new_block.distance = 10
            self.blocks.append(new_block)

    def increase_speed(self):
        self.distance+=5

    def move(self):
        for ii in self.blocks:
            ii.forward(ii.distance)