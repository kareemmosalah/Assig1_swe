from pizza import Pizza, ToppingDecorator
from payment import PayPal, CreditCard
from inventory import InventoryManager

def main():
    inventory = InventoryManager()

    # Create a Margherita Pizza
    base_pizza = Pizza(description="Margherita", cost=10)

    # Add Toppings (Cheese and Olives)
    if inventory.use_ingredient("Cheese"):
        base_pizza = ToppingDecorator(base_pizza, "Cheese", 1)
    if inventory.use_ingredient("Olives"):
        base_pizza = ToppingDecorator(base_pizza, "Olives", 0.5)

    # Display Pizza Details
    print("Order Summary:")
    print(f"Description: {base_pizza.get_description()}")
    print(f"Total Cost: ${base_pizza.get_cost():.2f}")

    # Choose Payment Method
    print("\nPayment:")
    payment_method = CreditCard()
    print(payment_method.pay(base_pizza.get_cost()))

    # Display Remaining Inventory
    print("\nRemaining Inventory:")
    print(inventory.get_inventory())


if __name__ == "__main__":
    main()