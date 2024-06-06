#Number Guessing Game Objectives:
import random
from replit import clear
logo="""
                              _   _                                  _               
                             | | | |                                | |              
   __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
  / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
   __/ |                                                                             
  |___/                                                                              
  """
print(logo)
def mode():
  mode= input("Would you like to play on easy or hard mode? Type 'easy' or 'hard': \n").lower()
  if mode=='easy':
    attempts=10
  if mode=='hard':
    attempts=5
  return attempts
  
chosen_number=random.randint(1,100)
attempts=mode()
game_over=0
while attempts>0 or game_over==0:
  guess_number=int(input("Guess a number between 1 and 100: \n"))
  if guess_number==chosen_number:
    print("You guessed the number correctly")
    game_over=1
    attempts=0
  elif guess_number>chosen_number:
    print("Your guess is higher than the number")
    attempts-=1
    print(f"You have {attempts} attempts left.")
  else:
    print("Your guess is lower than the number")
    attempts-=1
    print(f"You have {attempts} left.")
  if attempts==0 and game_over==0:
    print("You lose, you ran out of attempts.")
  if attempts==0 or game_over==1:
    ii=input("Would you like to play again? Type 'yes' or 'no': \n").lower()
    if ii=='yes':
      clear()
      attempts=mode()
      game_over=0
    else:
      game_over=1
      print("Thanks for playing!")
    

