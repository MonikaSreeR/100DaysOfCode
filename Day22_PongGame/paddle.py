from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()             
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.penup()
        self.goto(x=350, y=0)
        self.speed(0)

    def move_left(self):
        self.goto(x=-350, y=0)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(x=self.xcor(), y=new_y)
