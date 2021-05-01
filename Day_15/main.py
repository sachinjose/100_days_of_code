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
    "money" : 0.0
}


def input_amount(pennies, quarters, dimes, nickels):
    return pennies*0.01 + quarters*0.25 + dimes*0.10 + nickels*0.5


def deduct_resources(choice, money_entered):
    resources["water"] -= MENU[choice]['ingredients']['water']
    resources["milk"] -= MENU[choice]['ingredients']['milk']
    resources["coffee"] -= MENU[choice]['ingredients']['coffee']
    resources["money"] += money_entered


def check_resource(choice):
    flag = True
    if resources["water"] < MENU[choice]['ingredients']['water']:
        flag = False
        print("Sorry there is not enough water.")
    if resources["milk"] < MENU[choice]['ingredients']['milk']:
        flag = False
        print("Sorry there is not enough milk")
    if resources["coffee"] > MENU[choice]['ingredients']['coffee']:
        flag = False
        print("Sorry, there is not enough coffee")
    return flag


while(True):
    choice = input("What would you like ?")
    if choice == 'report':
        print(resources)
    elif choice == 'off':
        break
    else:
        if check_resource(choice):
            pennies = input("Enter the number of pennies : ")
            quarters = input("Enter the number of quarters : ")
            dimes = input("Enter the number of dimes : ")
            nickels = input("Enter the number of nickels : ")

            money_entered = input_amount(pennies, quarters, dimes, nickels)

            if money_entered < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded")

            else:
                deduct_resources(choice, money_entered)
                print("Here is your latte. Enjoy!")