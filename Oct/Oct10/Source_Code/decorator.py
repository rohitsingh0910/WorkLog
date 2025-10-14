class Coffee:
    def cost(self):
        return 5

class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())
