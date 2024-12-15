class Pizza:
    """Base class for Pizza."""
    def __init__(self, description="Basic Pizza", cost=0):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ToppingDecorator(Pizza):
    """Decorator class for dynamically adding toppings."""
    def __init__(self, pizza, topping_name, topping_cost):
        super().__init__()
        self.pizza = pizza
        self.topping_name = topping_name
        self.topping_cost = topping_cost

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.topping_name}"

    def get_cost(self):
        return self.pizza.get_cost() + self.topping_cost