# Pizza System

A simple Python application demonstrating the use of design patterns in a pizza restaurant ordering system.

## Features

- **Base Pizza**: Create basic pizza types (e.g., Margherita).
- **Dynamic Toppings**: Add one or more toppings dynamically.
  - Cheese: $1
  - Olives: $0.5
  - Mushrooms: $0.7
- **Inventory Management**: Ensure ingredients are available before adding toppings.
- **Payment Methods**: Simulate payment using PayPal or Credit Card.
- **Design Patterns Used**:
  - **Decorator**: For dynamic topping additions.
  - **Strategy**: For payment methods.
  - **Singleton**: For inventory management.

## Prerequisites

- Python 3.8 or later.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd PizzaSystem