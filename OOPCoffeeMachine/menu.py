class Menu():
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", cost=1.5, water=50, coffee=18),
            MenuItem(name="latte", cost=2.5, water=200, coffee=24, milk=150),
            MenuItem(name="cappuccino", cost=3.0,
                     water=250, coffee=24, milk=100),
        ]

    def get_items(self):
        lst = list(map(lambda x: x.name, self.menu))
        return '/'.join(lst)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print('Sorry that item is not available')
        return None


class MenuItem():
    def __init__(self, name, cost, water=0, milk=0, coffee=0):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
