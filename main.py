from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

machine_is_OFF = False

while not machine_is_OFF:

    user_welcome_input = input(f"What would you like? ({myMenu.get_items()}): ")

    if user_welcome_input == "off":
        print("Ok. See you...")
        machine_is_OFF = True

    elif user_welcome_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    else:
        user_choice = myMenu.find_drink(order_name=user_welcome_input)
        if user_choice is not None:
            print(f"You have chosen: {user_choice.name}")

            if my_coffee_maker.is_resource_sufficient(user_choice) and my_money_machine.make_payment(user_choice.cost):
                my_coffee_maker.make_coffee(user_choice)
