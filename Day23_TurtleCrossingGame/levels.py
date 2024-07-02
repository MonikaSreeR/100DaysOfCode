from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-380,270)
        self.write(f"LEVEL = {self.level}",font =("Arial",15,"normal"))

    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"LEVEL = {self.level}", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER and your highest winning level is {self.level -1}", align="Center",font=("Arial", 15, "normal"))