name = data[1]["Name"]
category = data [1]["Category"]
price = data[1]["Price"]
stock = data [1]["Stock"]

json_product = Product(name, category, price, stock)

json_product.show_info()