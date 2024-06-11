#####Turtle Intro######

import turtle as t
import random 



screen= t.Screen()
tim = t.Turtle()
t.shape('turtle')
screen.listen()
def move_forward():
  t.forward(10)
def move_backward():
  t.backward(10)
def move_counterclockwise():
  for angle in range(0,370,10):
    t.setheading(angle)
def move_clockwise():
  for angle in range(360,-10,-10):
    t.setheading(angle)
def turn_left():
  new_angle = t.heading() + 10
  t.setheading(new_angle)
def turn_right():
  new_angle = t.heading() - 10
  t.setheading(new_angle)
def clear():
  t.clear()
  t.home()
  t.clear()
    
  
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(move_counterclockwise,'a')
screen.onkey(move_clockwise, 'd')
screen.onkey(turn_left, 'q')
screen.onkey(turn_right, 'e')
screen.onkey(clear, 'c')







screen.exitonclick()
