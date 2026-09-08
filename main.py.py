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
        result = self.search_product_by_name(name)
        if result is not None:
            self.products.remove(result)

    def show_products(self):
        for product in self.products:
            product.show_info()

    def search_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        print("Product not found")

    def search_product_by_category(self, category):
        product_by_category = []
        for product in self.products:
            if product.category == category:
                product_by_category.append(product)
        if not product_by_category: 
            print("Category not found")
        return product_by_category


    def update_product(self, name, price):
        result = self.search_product_by_name(name)
        if result is not None:
            result.update_price(price)

    def low_stock(self, stock):
        low_stock_products = []
        for product in self.products:
            if product.stock <= stock:
                low_stock_products.append(product)
        if not low_stock_products:
            print("No products found")
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
        elif price <= 0:
            raise ValueError("Price must be greater than zero.")
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
            raise ValueError("Stock amount must be greater than zero.")
        self.stock += stock

    def remove_stock(self, stock):
        if not isinstance(stock, int):
            raise ValueError("Stock must be an integer number.")
        elif stock <= 0:
            raise ValueError("Stock must be greater than zero.")
        if self.stock >= stock:
            self.stock -= stock
        else:
            print("Not enough stock")

    def update_price(self, price):
        if not isinstance(price, (int,float)):
            raise ValueError("Price must be a number.")
        elif price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.price = price

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
    confirmation = input ("Please make sure the information is correct. Type 1 to confirm and add the product or type 2 to start over: ")
    if confirmation == "1":
        inventory.add_product(product_to_add)
        return False
    elif confirmation == "2":
        return True
    else:
        print("Please choose a correct option: 1 or 2.")
        return True

def search_product_option():
    print("""===== SEARCH MENU =====
1. Search by name
2. Search by category
3. Return to main menu""")
    search_selection = input ("Please choose an option: ")
    if search_selection == "1":
        print("Search by name selected.")
        search_product = input("Please type here to search your product: ")
        product = inventory.search_product_by_name(search_product)
        if product is not None:
            product.show_info()
        return True
    elif search_selection == "2":
        print("Search by category selected.")
        search_product = input("Please type here to search your product: ")
        category_list = inventory.search_product_by_category(search_product)
        for product in category_list:
            product.show_info()
        return True
    elif search_selection == "3":
        return False
    else:
        print("Please choose a correct option: 1, 2 or 3.") 
        return True   

def update_product_option():
    name = input("Please type the product name you want to update: ")
    price = input("Please type the new price amount: ")
    try:
        price = float(price)
    except ValueError:
        print("Price must be a number.")
        return True
    product = inventory.search_product_by_name(name)
    if product is not None:
        print("Product before changes:")
        product.show_info()
        try:
            inventory.update_product(name, price)
            print("Product after changes:")
            product.show_info()
        except ValueError as error:
            print(error)

def delete_product_option():
    name = input("Please type the name of the product to be removed: ")
    product = inventory.search_product_by_name(name)
    if product is None:
        return True
    product.show_info()
    while True:
        confirm_selection = input("""Are you sure you want to delete the follwing product? Please choose an option:
1. Confirm and delete product
2. Search again
3. Return to the main menu""")
        if confirm_selection == "1":
            inventory.delete_product(name)
            return False
        elif confirm_selection == "2":
            return True
        elif confirm_selection == "3":
            return False
        else:
            print("Please choose a correct option from 1 to 3: ")
    


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
        print("You have selected -Add product-")
        add_product_running = True
        while add_product_running:
            add_product_running = add_products_option()
    elif option == "2":
        print("You have selected -View product-")
        inventory.show_products()
    elif option == "3":
        print("You have selected -Search product-")
        search_product_running = True
        while search_product_running:
            search_product_running = search_product_option()
    elif option == "4":
        print("You have selected -Update product-")
        update_product_option()
    elif option == "5":
        delete_product_running = True
        while delete_product_running:
            delete_product_running = delete_product_option()