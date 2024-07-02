from turtle import Turtle


class Scoreboard(Turtle):
    left_score = 0
    right_score = 0
    def __init__(self,alignment):
        super().__init__()
        self.color("white")
        self.points = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        if alignment in ("right","left"):
            self.write(f"Score: {self.points} ", align=alignment, font=("arial", 15, "normal"))
            if alignment =="right":
                self.goto(300,275)
            if alignment =="left":
                self.goto(-300,275)

    def score_up(self,alignment):
        if alignment =="right":
            Scoreboard.right_score+=1
        elif alignment =='left':
            Scoreboard.left_score+=1

        self.points += 1
        self.clear()
        self.write(f"Score: {self.points} ", align=alignment, font=("arial", 15, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.clear()
        if Scoreboard.right_score>Scoreboard.left_score:
            self.winner = "winner is right paddle"
        elif Scoreboard.right_score<Scoreboard.left_score:
            self.winner = "winner is left paddle"
        else:
            self.winner = "It's a tie!"
        self.write(f"GAME OVER and  {self.winner}", align='center', font=("arial", 15, "normal"))
