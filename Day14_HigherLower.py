
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data import data
from replit import clear
import random


def display(item1,item2):           
    print (f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}")
    print(vs)
    #print("\n")
    print (f"Against B: {item2['name']}, a {item2['description']}, from {item2['country']} \n")

print(logo)
play_game = input("Would you like to play higher lower game? Type 'y' or 'n': ").lower()
while play_game=='y':
    clear()
    score=0  
    game_still_going =True
    item1= random.choice(data)
    while game_still_going:
        item2 = random.choice(data)
        while item1 == item2:
            item2 = random.choice(data)
        follower_count1 = item1['follower_count']
        follower_count2 = item2['follower_count']
        display(item1, item2)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (user_choice == 'a'and follower_count1 > follower_count2) or (
            user_choice == 'b'and follower_count2 > follower_count1):
            score+=1
            clear()
            print(logo)            
            print(f"You are right, your score is {score}")
            item1=item2
        else:
            print(f"You lost, your final score is {score}")
            game_still_going =False
            play_game = input("Would you like to play a new game? Type 'y' or 'n': ").lower()
            if play_game=='n':
                print("Thanks for playing the game!!")
        
