class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []

    def __str__(self):
        return f"Pizza: {self.size} size, {self.crust} crust, Toppings: {', '.join(self.toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza

pizza = PizzaBuilder().set_size('Large').set_crust('Thin').add_topping('Mushrooms').add_topping('Cheese').build()
print(pizza)
