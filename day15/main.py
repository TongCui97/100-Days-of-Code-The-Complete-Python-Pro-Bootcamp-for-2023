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

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
    if choice == 'off':
        is_on = False

    # TODO: 3. Print report of all coffee machine resources
    while choice == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
        choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 4. Check resources sufficient to make drinks
    for drink in MENU:
        if drink == choice:
            water_needed = MENU[drink]['ingredients']['water']
            # print(water_needed)
            coffee_needed = MENU[drink]['ingredients']['coffee']
            # print(coffee_needed)
            if choice == 'latte' or choice == 'cappuccino':
                milk_needed = MENU[drink]['ingredients']['milk']
                # print(milk_needed)

    if water_needed > water:
        print("Sorry there is not enough water.")
    elif coffee_needed > coffee:
        print("Sorry there is not enough coffee.")
    elif (choice == 'latte' or choice == 'cappuccino') and milk_needed > milk:
        print("Sorry there is not enough milk.")
    else:
        print("Please inset coins.")

    # TODO: 5. Process coins
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        penny = int(input("how many pennies?: "))
        total = quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01

        for drink in MENU:
            if drink == choice:
                price = MENU[drink]['cost']

        if price > total:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total - price
            change = round(change, 2)
            print(f"Here is ${change} in change")
            money += price

    # TODO: 6. Make Coffee
        water -= water_needed
        coffee -= coffee_needed
        if choice == 'latte' or choice == 'cappuccino':
            milk -= milk_needed
        print(f"Here is your {choice} ☕. Enjoy!")










