resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
menu = {
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


def print_report():
    for item in resources:
        print(f'{item}: {resources[item]}')


def check_resources_sufficient(order_ingredients):
    lst = list(
        filter(lambda item: order_ingredients[item] > resources[item], order_ingredients))
    if len(lst) > 0:
        print(f'Sorry! There is not enough {", ".join(lst)}.')
        return False
    else:
        return True


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.☕ Enjoy!")


def insert_coins():
    print('Please insert coins: ')
    total = 0
    total += int(input('How many quarters: ')) * 0.25
    total += int(input('How many dimes: ')) * 0.1
    total += int(input('How many nickles: ')) * 0.05
    total += int(input('How many pennies: ')) * 0.01
    return total


def main():
    is_on = True

    while is_on:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print_report()
        elif choice not in menu:
            print('Please choose one of three drinks above')
        else:
            drink = menu[choice]
            (ingredients, cost) = (drink["ingredients"], drink["cost"])
            if check_resources_sufficient(ingredients):
                payment = insert_coins()
                if payment < cost:
                    print('Sorry! That is not enough money. Money refund.')
                else:
                    if payment > cost:
                        print(
                            f'Here is ${round(payment - cost,2)} dollars in change')
                    resources["money"] += cost
                    make_coffee(choice, ingredients)


if __name__ == '__main__':
    main()
