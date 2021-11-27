class CoffeeMaker:
    def __init__(self, material_dict):
        self.resources = material_dict

    def report(self):
        for (key, value) in self.resources.items():
            print(f'{key}: {value}')

    def is_resource_sufficient(self, drink):
        lst = list(
            filter(lambda x: drink.ingredients[x] > self.resources[x], drink.ingredients.keys()))
        if len(lst) > 0:
            print(f'Sorry! There is not enough {", ".join(lst)}.')
            return False
        else:
            return True

    def make_coffee(self, order):
        for (key, value) in order.ingredients.items():
            self.resources[key] -= value
        print(f"Here is your {order.name}.☕ Enjoy!")
