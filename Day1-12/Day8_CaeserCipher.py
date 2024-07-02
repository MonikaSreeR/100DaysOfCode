logo="""
   _____                                  _       _               
  / ____|                                (_)     | |              
 | |     __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    
                                           """

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet= alphabet*2

def input_texts():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift%=26
    return direction, text, shift

def task(text, shift, direction):
    if direction=="decode":
        shift= shift*-1
    new_text= ""
    for ii in text:
        if ii in alphabet:
            index= alphabet.index(ii)
            new_index= index+shift
            new_text+= alphabet[new_index]
        else:
            new_text+= ii
    print(f"Your {direction}d text is {new_text}")

print(logo)
use_again=True
direction, text, shift = input_texts()

while use_again==True:
    task(text, shift, direction)
    ii=input("Do you want to use caeser cipher again, type y or n?\n")
    if ii=='n':
        use_again=False
        print("Good bye!") 
    elif ii=='y':
        direction, text, shift= input_texts()
        
        
    
    
    
        

