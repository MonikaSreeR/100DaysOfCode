#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                 
    '''                
from hangmanwords import word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
len_chosen_word = len(chosen_word)
guess_word='_'*len_chosen_word
print(logo)
lives=6
guess_word_list=[*guess_word]
while guess_word!=chosen_word:
  guess_letter=input("Guess a letter: ").lower()
  if guess_letter in guess_word:
    print("You already guessed this letter")
  if guess_letter in chosen_word:
    for i in range(len_chosen_word):
      if guess_letter==chosen_word[i]:
        guess_word_list[i]=guess_letter
    guess_word=''
    for ii in guess_word_list:
      guess_word+=ii
    print(guess_word)
  else:
    print("Guessed letter is not in the word")
    lives-=1
    print(stages[lives])
    if lives==0:
      print("You lost all lives")
      print(f"The word is {chosen_word}")
      break
    else:
      print(f"You have {lives} lives left")

if guess_word==chosen_word:
  print("YOU WON!!")

