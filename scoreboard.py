from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.points =0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.points} ", align="center", font=("arial",15,"normal"))


    def update(self):
        self.points +=1
        self.clear()
        self.write(f"Score: {self.points} ", align="center", font=("arial",15,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER and score is {self.points}", align='center', font=("arial",15,"normal"))
