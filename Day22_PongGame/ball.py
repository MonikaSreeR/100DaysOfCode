from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_move=10
        self.y_move=10

    def move(self):
        #self.setheading(10)
        self.penup()
        #self.speed(0)
        x=self.xcor() + self.x_move
        y=self.ycor() + self.y_move
        self.goto(x=x,y=y)

    def collision_with_wall(self):
        if self.ycor() >=280 or self.ycor()<=-280:
            self.y_move*=-1

    def bounce(self):
        self.x_move *=-1

    def restart(self):
        self.goto(0,0)



