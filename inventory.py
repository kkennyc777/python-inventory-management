import json
from product import Product

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
        
    def delete_product(self, product):
            self.products.remove(product)

    def show_products(self):
        for product in self.products:
            product.show_info()

    def search_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        

    def search_product_by_category(self, category):
        product_by_category = []
        for product in self.products:
            if product.category == category:
                product_by_category.append(product)
        return product_by_category

    def low_stock(self, stock):
        low_stock_products = []
        for product in self.products:
            if product.stock <= stock:
                low_stock_products.append(product)
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