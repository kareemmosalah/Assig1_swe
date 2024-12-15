class InventoryManager:
    """Singleton class to manage inventory."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.ingredients = {
                "Cheese": 10,
                "Olives": 10,
                "Mushrooms": 10
            }
        return cls._instance

    def is_available(self, ingredient):
        """Check if an ingredient is available."""
        return self.ingredients.get(ingredient, 0) > 0

    def use_ingredient(self, ingredient):
        """Use one unit of an ingredient."""
        if self.is_available(ingredient):
            self.ingredients[ingredient] -= 1
            return True
        return False

    def add_ingredient(self, ingredient, quantity):
        """Add a specific quantity of an ingredient."""
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

    def get_inventory(self):
        """Return the current inventory."""
        return self.ingredients