#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
logo="""
___________.__         _________        .__                      .__   __                
\__    ___/|__|_____   \_   ___ \_____  |  |   ____  __ _______  |  |_/  |_  ___________ 
  |    |   |  \____ \  /    \  \/\__  \ |  | _/ ___\|  |  \__  \ |  |\   __\/  _ \_  __ \
  |    |   |  |  |_> > \     \____/ __ \|  |_\  \___|  |  // __ \|  |_|  | (  <_> )  | \/
  |____|   |__|   __/   \______  (____  /____/\___  >____/(____  /____/__|  \____/|__|   
              |__|             \/     \/          \/           \/                        """

print("I will calculate the tip for you")
print(logo)
bill=float(input("What was the total bill? \n $"))
tip=int(input("How much percentage tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))
tip_as_percent = tip / 100
total_bill = bill*(1+tip_as_percent)
splitted_bill = total_bill / people
print(f"Each person has to pay ${splitted_bill}")
