from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def main():
    my_menu = Menu()
    coffee_maker = CoffeeMaker(resources)
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        choice = input(f"What would you like? ({my_menu.get_items()}): ")
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = my_menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
