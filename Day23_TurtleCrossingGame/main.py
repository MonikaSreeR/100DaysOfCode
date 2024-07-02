from turtle import Screen
import time
from player import Player
from movingblocks import Block
from levels import Level
DELAY=0.2

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Turtle Crossing Game")
screen.colormode(255)
screen.tracer(0)
blocks = Block()
player = Player()
screen.listen()
screen.onkey(player.move,"Up")
level = Level()

game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(DELAY)
    blocks.create_block()
    blocks.move()
    for ii in blocks.blocks:
        if player.distance(ii)<=20: #Detection of collision of turtle with moving block
            game_is_on =False
            level.game_over()
    if player.ycor()>=290: #Turtle successfully crossed the moving blocks
        level.level_up()
        player.start_position()
screen.exitonclick()
