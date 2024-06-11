import turtle as t
import random 

screen= t.Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Want to bet?', prompt='Which turtle will win the race? Enter a color: ')

y=-150
turtle_list=[]
for color in ['red','blue','green','yellow','orange','purple','indigo']:
  name = color+'_tim'
  name = t.Turtle()
  name.color(color)
  name.shape('turtle')
  name.penup()
  #name.setheading(angle)
  name.goto(x=-250,y=y)
  y = y + 50
  turtle_list.append(name)

#winner = 'lets see'
def race():
  while True:
    name =random.choice(turtle_list)   
    name.forward(random.randint(0,10))
    if name.xcor() > 230:         
      winner = name.pencolor()
      if winner == user_guess:
        print(f"You won the game, {winner} turtle is the winner. Congratulations!")
      else:
        print(f"You lost the game, {winner} turtle is the winner. Better luck next time!")      
      return 

screen.listen()
screen.onkey(race,'space')

screen.exitonclick()
