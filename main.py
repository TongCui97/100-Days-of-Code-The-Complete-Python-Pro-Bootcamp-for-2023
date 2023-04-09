from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_continue = True
while is_continue:
    options = menu.get_items()
    choice = input(f"What drink would you like? ({options}) ")
    if choice == 'off':
        is_continue = False
    # 1. Make a report
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # 2. check resources sufficient?
        check_resource = coffee_maker.is_resource_sufficient(drink)
        # 3. Process coins
        if check_resource:
            price = drink.cost
            # 4. check transaction successfully?
            if money_machine.make_payment(price):
                # 5. Make coffee
                coffee_maker.make_coffee(drink)









