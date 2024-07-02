logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
operations = {'+':add, '-':sub, '*':mul, '/':div}
key_list = list(operations.keys())
  
num1 = float(input("+"))
def calculator(num1): 
  for key in operations:    
    print(key)
  operator =input("Pick any of the above operators")
  if operator not in key_list:
    print("Invalid operator")
    return
  func = operations[operator]
  num2=float(input(f"What's the next number?\n"))
  answer = func(num1,num2)
  print(f"{num1} {operator} {num2} = {answer}")
  print(f"Type y to continue calculating with {answer} or type n to exit")
  if input() == 'y':
    num1 = answer
    calculator(answer)
  else:
    print("Thanks for using the calculator.")
    return

calculator(num1)
