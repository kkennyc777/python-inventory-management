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




class Product:

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def show_info(self):
        print(f"=== PRODUCT ===\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}\nStock: {self.stock}")

    def add_stock(self, stock):
        self.stock += stock

    def remove_stock(self, stock):
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

inventory = Inventory()

mouse = Product("Razer Mouse", "Mouse", 20, 15)
keyboard = Product("Logitech Keyboard", "Keyboard", 50, 8)
monitor = Product("Samsung Monitor", "Monitor", 200, 4)
headphones = Product("Sony Headphones", "Headphones", 80, 2)

inventory.add_product(mouse)
inventory.add_product(keyboard)
inventory.add_product(monitor)
inventory.add_product(headphones)

data = inventory.product_to_list()

json_data = json.dumps(data, indent=4)

print(json_data)
print(type(json_data))