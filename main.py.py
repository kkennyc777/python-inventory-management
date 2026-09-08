import json

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def product_to_list(self):
        product_information = []
        for product in self.products:
            data = product.to_dict()
            product_information.append(data)
        return product_information
        
    def delete_product(self, name):
        result = self.search_product(name)
        if result is not None:
            self.products.remove(result)

    def show_products(self):
        for product in self.products:
            product.show_info()

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        print("Product not found")

    def update_product(self, name, price):
        result = self.search_product(name)
        if result is not None:
            result.price = price

    def low_stock(self, stock):
        low_stock_products = []
        for product in self.products:
            if product.stock <= stock:
                low_stock_products.append(product)
        for product in low_stock_products:
            return low_stock_products

    def load_products(self):
        try:
            with open("products.json", "r") as file:
                data = json.load(file)
            self.products = []
            for product in data:
                name = product["Name"]
                category = product["Category"]
                price = product["Price"]
                stock = product["Stock"]
                json_product = Product(name, category, price, stock)
                self.add_product(json_product)
        except FileNotFoundError:
            print("No saved inventory found")
        except json.JSONDecodeError:
            print("Invalid inventory data.")
        except KeyError as error:
            print(f"Missing product field: {error.args[0]}")
        except ValueError as error:
            print(error)

    def save_products(self):
        data = self.product_to_list()
        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)


class Product:

    def __init__(self, name, category, price, stock):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        elif price < 0:
            raise ValueError("Price cannot be negative.")
        if not isinstance(stock, int):
            raise ValueError("Stock must be an integer number.")
        elif stock < 0:
            raise ValueError("Stock cannot be negative.")
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        elif not name.strip():
            raise ValueError("Name field cannot be empty.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        elif not category.strip():
            raise ValueError("Category field cannot be empty.")
        self.name = name.strip()
        self.category = category.strip()
        self.price = price
        self.stock = stock

    def show_info(self):
        print(f"=== PRODUCT ===\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}\nStock: {self.stock}")

    def add_stock(self, stock):
        if not isinstance(stock, int):
            raise ValueError("Stock must be a number.")
        elif stock <= 0:
            raise ValueError("Stock cannot be negative.")
        self.stock += stock

    def remove_stock(self, stock):
        if not isinstance(stock, int):
            raise ValueError("Stock must be a number.")
        elif stock <= 0:
            raise ValueError("Stock cannot be negative.")
        if self.stock >= stock:
            self.stock -= stock
        else:
            print("Not enough stock")

    def to_dict(self):
        product_to_dict = {"Name" : self.name,
         "Category" : self.category,
         "Price" : self.price,
         "Stock" : self.stock
        }
        return product_to_dict

def add_products_option():
    name = input ("Please enter the name of the product to be added: ")
    category = input ("Please enter the category of the product to be added: ")
    price = input ("Please enter the price of the product to be added: ")
    try:
        price = float(price)
    except ValueError:
        print("Price must be a number.")
        return True
    stock = input ("Please enter the stock of the product to be added: ")
    try:
        stock = int(stock)
    except ValueError:
        print("Stock must be an integer number")
        return True
    try:
        product_to_add = Product(name, category, price, stock)
    except ValueError as error:
        print(error)
        return True
    print ("The following product will be added:")
    product_to_add.show_info()
    confirmation = input ("Please make sure the information is correct. Type 1 to confirm and save or type 2 to start over: ")
    if confirmation == "1":
        inventory.add_product(product_to_add)
        return False
    elif confirmation == "2":
        return True
    else:
        print("Please choose a correct option: 1 or 2.")
        return True

inventory = Inventory()
inventory.load_products()
program_running = True
while program_running:
    print("""========== INVENTORY SYSTEM ==========
1. Add product
2. View products
3. Search product
4. Update product
5. Delete product
6. View low-stock products
7. Save
8. Exit""")
    option = input("Welcome.\nPlease choose an option: ")
    if option == "1":
        add_product_running = True
        while add_product_running:
            add_product_running = add_products_option()
    elif option == "2":
        inventory.show_products()
