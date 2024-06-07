logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
from replit import clear

cards_list=[2,3,4,5,6,7,8,9,'J','Q','K','A']
cards_dict={'J':10,'Q':10,'K':10,'A':11}

def pick_card():
  return random.choice(cards_list)
def score(cards):
  score=0
  if len(cards)==2 and (cards ==['A',10] or cards==[10,'A']):
    return 0
  for card in cards:
    if card not in cards_dict:
      score+=card
    elif card in cards_dict:
      score+=cards_dict[card]
  if score>21 and 'A' in cards:
    score-=10
  return score

def compare(user_score,dealer_score):
  if user_score > 21 and dealer_score > 21:
    print("You went over. You lose")
  elif user_score==0:
    print("You win with a Blackjack!")
  elif dealer_score==0:
    print("Dealer wins with a Blackjack!")
  elif user_score>21:
    print("You went over. You lose!")
  elif dealer_score>21:
    print("Dealer went over. You win!")
  elif user_score==dealer_score:
    print("It's a draw!")
  elif user_score>dealer_score:
    print("You win the game!")
  elif user_score<dealer_score:
    print("You lose the game!")
  play_new_game=input("Do you want to play a new game? Type 'y' or 'n': ").lower()
  return play_new_game

print(logo)
play_new_game= input("Do you want to play Black Jack game? Type 'y' or 'n': ").lower()
while play_new_game=='y':
  clear()
  print(logo)
  user_cards=[pick_card(),pick_card()]
  dealer_cards=[pick_card()]
  user_score = score(user_cards)
  dealer_score = score(dealer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {dealer_cards}")
  if score(user_cards)==0:
    compare(user_score,dealer_score)
  else:
    another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while another_card=='y':
      user_cards.append(pick_card())
      user_score=score(user_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    
    if another_card=='n':
      while dealer_score<17:
        dealer_cards.append(pick_card())
        dealer_score=score(dealer_cards)
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    play_new_game=compare(user_score,dealer_score)
      
      
      
    





































############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#create cards list
#Pick 1 dealer card
#Pick 2 player cards
#Calculate player score
#Calculate dealer score
#If sum<21, ask player if they want another card
#If sum>21, check if ace is present, if yes, change
#Once player stop picking cards, dealer picks cards until sum>17
