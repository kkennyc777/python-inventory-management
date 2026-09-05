inventory.add_product(mouse)
inventory.add_product(keyboard)
inventory.add_product(monitor)
inventory.add_product(headphones)

result = inventory.low_stock(5)
if not result:
    print("No coincidences found.")
for product in result:
    product.show_info()
