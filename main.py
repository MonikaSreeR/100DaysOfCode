from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    #Food collision detection
    if snake.head.distance(food) < 15:
        food.relocate()
        score.update()
        snake.add_segment()
    #Detect snake collision with wall
    if snake.head.xcor() > 288 or snake.head.xcor() <= -288 or snake.head.ycor() > 288 or snake.head.ycor() <= -288:
        game_is_on = False
        score.gameover()
    #Detect snake collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()

screen.exitonclick()
