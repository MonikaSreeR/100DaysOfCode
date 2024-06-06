from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")
dict={}
next_bidder=True
while next_bidder == True:
  name= input("What is your name?\n ")
  bid=float(input("How much would you like to bid?\n $ "))
  dict[name]=bid
  next_bidder = input("Is there another bidder? Type 'yes' or 'no'\n ").lower()
  if next_bidder == "yes":
    clear()
    next_bidder=True
  else:
    next_bidder=False

max_bid=0
for key in dict:
  if dict[key]>max_bid:
    max_bid=dict[key]
    max_bid_name=key
print(f"{max_bid_name} has won the bid with a bid of ${max_bid}")
