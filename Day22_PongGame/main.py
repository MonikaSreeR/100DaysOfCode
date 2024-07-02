from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
l_paddle.move_left()
ball = Ball()
score_right = Scoreboard("right")
score_left = Scoreboard("left")
game_over = Scoreboard("dummy")

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down,'p')

game_point=11
game_is_on = True
delay =0.1
while game_is_on:
    time.sleep(delay)
    screen.update()
    ball.move()
    ball.collision_with_wall()

    #detection of collison with paddles
    if (ball.xcor()>= 340 and ball.distance(r_paddle)<=50) or (ball.xcor()<=-340 and ball.distance(l_paddle)<=50):
        ball.bounce()
        delay*=0.9

    elif ball.xcor()>=380:
        score_left.score_up("left")
        ball.restart()
        ball.bounce()

    elif ball.xcor()<=-380:
        score_right.score_up("right")
        ball.restart()
        ball.bounce()

    #Stop game at game point
    if Scoreboard.left_score ==game_point or Scoreboard.right_score==game_point:
        game_is_on =False



if game_is_on == False:
    game_over.gameover()



screen.exitonclick()

