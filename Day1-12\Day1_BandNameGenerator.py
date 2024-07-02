#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
logo = """
__________                    .___  _______                            ________                                   __                
\______   \_____    ____    __| _/  \      \ _____    _____   ____    /  _____/  ____   ____   ________________ _/  |_  ___________ 
 |    |  _/\__  \  /    \  / __ |   /   |   \\__  \  /     \_/ __ \  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
 |    |   \ / __ \|   |  \/ /_/ |  /    |    \/ __ \|  Y Y  \  ___/  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 |______  /(____  /___|  /\____ |  \____|__  (____  /__|_|  /\___  >  \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/      \/     \/      \/          \/     \/      \/     \/          \/     \/     \/     \/           \/                   
        
"""
print(logo)
#2. Ask the user for the city that they grew up in.
city =input("Please tell us the city you grew up in? \n").title()
#3. Ask the user for the name of a pet.
pet =input("What's the name of your pet? \n").title()
#4. Combine the name of their city and pet and show them their band name.
print(f"Your band name is {city} {pet}")
