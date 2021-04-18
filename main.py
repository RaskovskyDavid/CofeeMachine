

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
money = 0
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

def check_what_would_be(MENU_check):
    keep_asking = True
    while keep_asking:
        print("Welcome to the coffee machine")
        print("You can drink\n")
        option = 0
        for drink in MENU_check:
            option += 1
            drink_dictionary = MENU_check[drink]
            drink_name = drink
            cost_of_drink = drink_dictionary['cost']
            print(f"Choose option {option} for  {drink_name} cost {cost_of_drink}")
        what_would_be = input("What would it be Type: ")
        if what_would_be.isnumeric():
            keep_asking = False
            return list(MENU_check)[int(what_would_be)-1] # int(what_would_be)
        else:
            if what_would_be.lower() == 'off':
                keep_asking = False
                return what_would_be.lower()
            else:
                keep_asking = True



# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def print_report(resources_report, money_report):
    print("REPORTING RESOURCES")
    for resource in resources_report:
        name = resource
        quantity = resources_report[resource]
        print(f"{name} {quantity}")
    print(f"Money get for selling: {money_report}")
    return

# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def check_its_sufficient(drink_id, drink_dictionary, resource_stock):
    ingredient_ok = 0
    recipe = drink_dictionary[drink_id]["ingredients"]
    for need_recipe in recipe:
        need_quantity = recipe[need_recipe]
        if  resource_stock[need_recipe] -need_quantity < 0:
            ingredient_ok = 1
            print(f"There is no {need_recipe} for make the {drink_id}")
    if ingredient_ok > 0:
        print(f"Try other drink or ask for help to refill the machine")
    return ingredient_ok



# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def coins_paiment_count():
    quarters = int(input("Inserts coins of quarters: "))
    dimes = int(input("Inserts coins of dimes: "))
    nickles = int(input("Inserts coins of nickles: "))
    pennies = int(input("Inserts coins of pennies: "))
    paiment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    return paiment
# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def coins_paiment(drink_id, menu, paiment):
    cost = menu[drink_id]["cost"]
    while paiment < cost:
        print(f"For make a {drink_id} the cost its: ${cost} you enter ${paiment}")
        quarters = int(input("Inserts coins of quarters: "))
        dimes = int(input("Inserts coins of dimes: "))
        nickles = int(input("Inserts coins of nickles: "))
        pennies = int(input("Inserts coins of pennies: "))
        paiment += 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        quarters = 0
        dimes = 0
        nickles = 0
        pennies = 0
        if paiment < cost:
            refound = input("You don't have enough money do you want to keep trying or a refund? Type 'r' for refund: ")
            if refound == 'r':
                print("Refund")
                return 0
    if paiment > cost:
        print(f"Your exchange its : ${round(paiment - cost, 2) }")
    return cost

# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink
def make_drink(drink_id, drink_dictionary, resource_stock):
    recipe = drink_dictionary[drink_id]["ingredients"]
    for need_recipe in recipe:
        need_quantity = recipe[need_recipe]
        resource_stock[need_recipe] -= need_quantity
    print(f"Here is your {drink_id} . Enjoy!")
    return 0

def coffee_machine(MENU_coffee_machine,  resources_coffee_machine, money):
    on = True
    while on:
        print("Welcome to the cofee machine")
        money_coffee_machine = coins_paiment_count()
        drink = check_what_would_be(MENU_coffee_machine)
        if drink == 'off':
            print("The machine is power off good bye")
            on = False
        else:
            money_coffee_machine = coins_paiment(drink, MENU_coffee_machine, money_coffee_machine)
            if money_coffee_machine > 0:
                ingredient_ok = check_its_sufficient(drink, MENU_coffee_machine, resources_coffee_machine)
                if ingredient_ok == 0:
                    print_report(resources_coffee_machine, money)
                    money += money_coffee_machine
                    make_drink(drink, MENU_coffee_machine, resources_coffee_machine)
                    print_report(resources_coffee_machine, money)



coffee_machine(MENU, resources, money)