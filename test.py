class Product:

    def __init__(self, name, category, price, stock):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
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
        update_price = price
        if not isinstance(update_price, float):
            raise ValueError("Price must be a number.")
        elif update_price <= 0:
            raise ValueError("Price cannot be negative")
        self.price = price
        self.stock = stock