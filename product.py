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
