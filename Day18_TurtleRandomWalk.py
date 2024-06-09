#####Turtle Intro######

import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("pink")
#colors = ["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink"]
screen= t.Screen()
screen.colormode(255)
timmy.speed("fastest")
timmy.pensize(10)


def action():
  angle = [0, 90, 180, 270]
  timmy.forward(random.randint(10,50))
  timmy.right(random.choice(angle))
  
  #action = ['forward','backward', 'right', 'left']
  #act = random.choice(action)
  #if act == "right":
  #  timmy.right(90)
  #elif act =="left":
  #  timmy.left(90)
  #  
  #if act in ["forward", "backward"]:
  #  steps = random.randint(10,50)
  #  if act == "forward":
  #    timmy.forward(steps)
  #  elif act =="backward":
  #    timmy.backward(steps)
    
  
  
for _ in range(500):
  timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  action() 


screen.exitonclick()
