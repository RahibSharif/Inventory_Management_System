import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
product_path = BASE_DIR / "products.json"

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
        "Name": self.name,
        "Quantity": self.quantity,
        "Price": self.price
        }

inventory = []

def add_product():
        name = input("Enter name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))     

        product = Product(name, quantity, price)

        inventory.append(product)
        print("Successfully added!")   


def view_products():
     for product in inventory:
        print()
        print(f"Name: {product.name}")
        print(f"Quantity: {product.quantity}")
        print(f"Price: ${product.price}")

def load_products():
    if product_path.exists():
        with open(product_path, "r") as f:
            products = json.load(f)

        for item in products:
            product = Product(
                item["Name"],
                item["Quantity"],
                item["Price"]
            )
            inventory.append(product)

load_products()

def delete_product():
    name = str(input("Enter name: "))

    for product in inventory:
        if product.name.lower() == name.lower():
            inventory.remove(product)
            print("Product deleted!")
            return

def update_quantity():
    name = input("Enter product name: ")

    for product in inventory:
        if product.name.lower() == name.lower():
            new_quantity = int(input("Enter new quantity: "))
            product.quantity = new_quantity
            print("New quantity added!")
            return
        
    print("Product not found!")
        
def search_product():
    name = input("Enter product name: ")

    for product in inventory:
        if product.name.lower() == name.lower():
            print()
            print(f"Name: {product.name}")
            print(f"Quantity: {product.quantity}")
            print(f"Price: ${product.price}")
            return
    
    print("Product not found!")

def update_price():
    name = input("Enter product name: ")

    for product in inventory:
        if product.name.lower() == name.lower():
            updated_price = float(input("Enter new price: "))
            product.price = updated_price
            print("Price updated!")
            return
    
    print("Product not found!")

def total_inventory_value():
    total = 0

    for product in inventory:
        total += product.quantity * product.price
    
    print(f"Total inventory value: {total:.2f}")

def low_stock():
    for product in inventory:
        if product.quantity < 5:
            print(f"{product.name} is low on stock!")
            return
    print("No products are low on stock!")

menu = """
1. Add product.
2. View product.
3. Quit.
4. Delete product.
5. Update quantity.
6. Search product.
7. Update price.
8. Total inventory value.
9. Low stock alert.
"""

while True:
    print(menu)
    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

        with open(product_path, "w") as f:
            json.dump([product.to_dict() for product in inventory], f)

    elif choice == "2":
        view_products()

    elif choice == "3":
        print("Goodbye!")
        break 

    elif choice == "4":
        delete_product()

        with open(product_path, "w") as f:
            json.dump([product.to_dict() for product in inventory], f)

    elif choice == "5":
        update_quantity()

        with open(product_path, "w") as f:
            json.dump([product.to_dict() for product in inventory], f)

    elif choice == "6":
        search_product()

    elif choice == "7":
        update_price()

        with open(product_path, "w") as f:
            json.dump([product.to_dict() for product in inventory], f)

    elif choice == "8":
        total_inventory_value()

    elif choice == "9":
        low_stock()

    else:
        print("Invalid option!")       
     
