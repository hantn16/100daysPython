class MoneyMachine():
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self, profit=0):
        self.profit = profit
        self.received_money = 0

    def report(self):
        print(f'money: {self.profit}')

    def process_coins(self):
        print('Please insert coins: ')
        for (key, value) in self.COIN_VALUES.items():
            self.received_money += int(input(f'How many {key}: ')) * value
        return self.received_money

    def make_payment(self, cost):
        money_received = self.process_coins()
        if money_received >= cost:
            change = round(money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.received_money = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.received_money = 0
            return False
