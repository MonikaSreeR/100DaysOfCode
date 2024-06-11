

import turtle as t
import random 


colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.right(90)
tim.forward(250)
tim.right(90)
tim.forward(200)
tim.left(180)
for ii in range(1,101):
  tim.dot(20,random.choice(colors))
  tim.forward(50)
  if ii%10==0:
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)






screen= t.Screen()
screen.exitonclick()
