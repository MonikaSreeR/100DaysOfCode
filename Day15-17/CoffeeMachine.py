MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def price(choice, in_dollars):
    cost = MENU[choice]['cost']
    out_dollars = round((in_dollars - cost),2)
    global income
    income+=cost
    return out_dollars

def make_coffee(choice):
    for key in MENU[choice]["ingredients"]:
        resources[key] -= MENU[choice]["ingredients"][key]
    print(f"Here is your {choice} ☕. Enjoy!")


def resource_check(choice):
    for key in MENU[choice]["ingredients"]:
        if resources[key] >= MENU[choice]["ingredients"][key]:
            continue
        else:
            print(f"Sorry insufficient {key}!")
            return False
    return True

def process_coins(choice,total_dollars):
    change = price(choice, total_dollars)
    if change < 0:
        print("Sorry that's not enough money. Money refunded")
    elif change == 0:
        print("That's sufficient money.")
        make_coffee(customer_input)
    else:
        print(f"Here is ${change} as change.")
        make_coffee(customer_input)

income =0
is_on = True
while is_on:
    customer_input = input("What would you like to have? (espresso/latte/cappuccino) \n ").lower()
    if customer_input =='off':
        is_on = False
    elif customer_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Income: ${income}.")

    elif customer_input in ['espresso','latte','cappuccino']:
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_dollars = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if resource_check(customer_input):
            process_coins(customer_input, total_dollars)

    else:
        print("Invalid input!")





