# LibraryAPI and PizzaSystem Projects

## Overview
This repository contains two projects:

1. **LibraryAPI**: A RESTful API for managing a library's collection of books, implemented using Flask.
2. **PizzaSystem**: A Python application demonstrating design patterns for a pizza ordering system.

---

## LibraryAPI

### Description
The LibraryAPI is a RESTful API for managing a library's collection of books. It allows the following operations:
- Add a new book.
- List all books.
- Search for books by author, genre, or published year.
- Update book details by ISBN.
- Delete a book by ISBN.

The API includes:
- Swagger UI for API documentation and testing.
- Dockerized environment for easy setup and deployment.

---

### Folder Structure
```plaintext
LibraryAPI/
├── src/
│   ├── app.py                       # Main Flask application
│   ├── models/
│   │   └── books.json               # JSON file for data storage
│   ├── routes/
│   │   └── books_routes.py          # Route handlers for books
│   └── controllers/
│       └── books_controller.py      # Controller logic for book operations
├── Dockerfile                       # Docker instructions
├── docker-compose.yml               # Docker Compose setup
├── requirements.txt                 # Python dependencies
├── README.md                        # Project setup and usage instructions
├── static/
│   └── swagger.json                 # Swagger API documentation
├── tests/
│   └── test_books.py                # Test cases for API
└── .github/
    └── workflows/
        ├── pre-merge.yml            # CI workflow for pull requests
        ├── component-build.yml      # Build and test workflow
        └── deployment.yml           # Deployment workflow

How to Run LibraryAPI

Prerequisites
	•	Python 3.9 or later
	•	Docker and Docker Compose

Running Locally
	1.	Clone the repository:

git clone <repository_url>
cd LibraryAPI


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Run the application:

python src/app.py


	4.	Access the API:
	•	Base URL: http://localhost:5000
	•	Swagger UI: http://localhost:5000/api-docs

Running with Docker
	1.	Build the Docker image:

docker-compose build


	2.	Start the container:

docker-compose up


	3.	Access the API:
	•	Base URL: http://localhost:5000
	•	Swagger UI: http://localhost:5000/api-docs

Running Tests
	1.	Ensure you have pytest installed:

pip install pytest


	2.	Run the test cases:

pytest tests/

PizzaSystem

Description

The PizzaSystem is a Python application that demonstrates the use of design patterns in a pizza ordering system. The system supports:
	•	Creating a base pizza (e.g., Margherita or Pepperoni).
	•	Adding dynamic toppings like Cheese, Olives, and Mushrooms.
	•	Managing inventory for ingredients.
	•	Implementing multiple payment methods (e.g., PayPal or Credit Card).

Folder Structure

PizzaSystem/
├── pizza.py              # Pizza and Topping classes
├── payment.py            # Payment methods
├── inventory.py          # Singleton inventory management
├── main.py               # Entry point
├── README.md             # Documentation

How to Run PizzaSystem

Prerequisites
	•	Python 3.8 or later

Running the Application
	1.	Clone the repository:

git clone <repository_url>
cd PizzaSystem


	2.	Run the main script:

python main.py



Example Output

Order Summary:
Description: Margherita, Cheese, Olives
Total Cost: $11.50

Payment:
Paid $11.50 using Credit Card.

Remaining Inventory:
{'Cheese': 9, 'Olives': 9, 'Mushrooms': 10}

Design Patterns Used

LibraryAPI
	1.	Separation of Concerns: Organized into routes, controllers, and models to keep responsibilities clear.
	2.	CI/CD Pipelines: Automates testing and deployment using GitHub Actions.

PizzaSystem
	1.	Decorator Pattern: Dynamically adds toppings to the base pizza without modifying the Pizza class.
	2.	Singleton Pattern: Ensures only one InventoryManager instance exists to manage inventory.
	3.	Strategy Pattern: Enables flexible selection of payment methods (e.g., PayPal or Credit Card).

GitHub Repository Submission
	1.	Create a public GitHub repository named LibraryAPI_PizzaSystem.
	2.	Push all files to the repository:

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repository_url>
git push -u origin main


	3.	Submit:
	•	A ZIP file containing the folder named <YourName>_<YourSection>_<YourID> with:
	•	LibraryAPI/ and PizzaSystem/ folders.
	•	The GitHub repository URL.

Let me know if further clarifications or adjustments are required!

