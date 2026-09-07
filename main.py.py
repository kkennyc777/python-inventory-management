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

    def save_products(self):
        data = self.product_to_list()
        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)


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
inventory.load_products()

webcam = Product("UGREEN", "Accesories", 5, 10 )
inventory.add_product(webcam)

inventory.show_products()
inventory.save_products()
inventory.show_products()




