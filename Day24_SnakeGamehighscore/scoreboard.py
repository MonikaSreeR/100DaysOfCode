from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.points =0
        with open("HighestScore.txt") as hs:
            #a =hs.read()
            self.highestscore = int(hs.read())
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.points} Highest Score: {self.highestscore}", align="center", font=("arial",15,"normal"))



    def update(self):
        self.points +=1
        if self.points> self.highestscore:
            self.highestscore +=1
        with open("HighestScore.txt", 'w') as hs:
            hs.write(str(self.highestscore))
        self.clear()
        self.write(f"Score: {self.points} Highest Score: {self.highestscore} ", align="center", font=("arial",15,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER and score is {self.points} and Highest Score: {self.highestscore}", align='center', font=("arial",15,"normal"))

    def reset(self):
        self.points=0
        self.clear()
        self.write(f"Score: {self.points} Highest Score: {self.highestscore} ", align="center", font=("arial",15,"normal"))


