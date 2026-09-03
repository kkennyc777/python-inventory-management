class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.show_info()

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        print("Product not found")
            



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

inventory = Inventory()

mouse = Product("Razer Mouse", "Mouse", 20, 15)
keyboard = Product("Logitech Keyboard", "Keyboard", 50, 8)
monitor = Product("Samsung Monitor", "Monitor", 200, 4)

inventory.add_product(mouse)
inventory.add_product(keyboard)
inventory.add_product(monitor)

result = inventory.search_product("Razer Mouse")
result.show_info()