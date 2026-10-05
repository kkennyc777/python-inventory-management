from product import Product
from inventory import Inventory

def add_products_option(inventory):
    print("You have selected -Add product-")
    while True: 
        name = input ("Please enter the name of the product to be added: ")
        category = input ("Please enter the category of the product to be added: ")
        price = input ("Please enter the price of the product to be added: ")
        try:
            price = float(price)
        except ValueError:
            print("Price must be a number.")
            continue
        stock = input ("Please enter the stock of the product to be added: ")
        try:
            stock = int(stock)
        except ValueError:
            print("Stock must be an integer number")
            continue
        try:
            product_to_add = Product(name, category, price, stock)
        except ValueError as error:
            print(error)
            continue
        print ("The following product will be added:")
        product_to_add.show_info()
        confirmation_loop = True
        while confirmation_loop:
            confirmation = input ("Please make sure the information is correct. Type -yes- to confirm and add the product or type -no- to edit the information: ")
            if confirmation == "yes":
                inventory.add_product(product_to_add)
                return
            elif confirmation == "no":
                print("Let's start over.")
                confirmation_loop = False
            else:
                print("Please choose a correct option: yes or no.")
                continue

def show_products_option(inventory):
    print("You have selected -View product-")
    inventory.show_products()

def search_product_option(inventory):
    print("You have selected -Search Product-")
    while True:
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
            else:
                print("Product not found")
            continue
        elif search_selection == "2":
            print("Search by category selected.")
            search_product = input("Please type here to search your product: ")
            category_list = inventory.search_product_by_category(search_product)
            if not category_list: 
                print("Category not found")
            else: 
                for product in category_list:
                    product.show_info()
            continue
        elif search_selection == "3":
            return
        else:
            print("Please choose a correct option: 1, 2 or 3.") 
            continue   

def update_product_option(inventory):
    print("You have selected -Update product-")
    name = input("Please type the product name you want to update: ")
    product = inventory.search_product_by_name(name)
    if product is not None:
        print("Product before changes:")
        product.show_info()
        price = input("Please type the new price amount: ")
        try:
            price = float(price)
        except ValueError:
            print("Price must be a number.")
            return
        try:
            product.update_price(price)
            print("Product after changes:")
            product.show_info()
        except ValueError as error:
            print(error)
    else:
        print("Product not found.")
        return

def delete_product_option(inventory):
    print("You have selected -Delete Product-")    
    while True:
        name = input("Please type the name of the product to be removed: ")
        product = inventory.search_product_by_name(name)
        if product is None:
            print ("Product not found.")
            continue
        product.show_info()
        while True:
            confirm_selection = input("""Are you sure you want to delete the follwing product? Please choose an option:
1. Confirm and delete product
2. Search again
3. Return to the main menu""")
            if confirm_selection == "1":
                inventory.delete_product(product)
                return
            elif confirm_selection == "2":
                break
            elif confirm_selection == "3":
                return
            else:
                print("Please choose a correct option from 1 to 3: ")

def low_stock_option(inventory):
    print("You have selected -View low-stock products-")
    stock = input("Please choose the amount of stock: ")
    try:
        stock = int(stock)
        result = inventory.low_stock(stock)
        if not result:
            print(f"There are no products with stock less than or equal to {stock}.")
        else:
            for product in result:
                product.show_info()
    except ValueError:
        print("Stock must be an integer number.")


def main():  
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
            add_products_option(inventory)
        elif option == "2":
            show_products_option(inventory)
        elif option == "3":
            search_product_option(inventory)
        elif option == "4":
            update_product_option(inventory)
        elif option == "5":
            delete_product_option(inventory)
        elif option == "6":
            low_stock_option(inventory)
        elif option == "7":
            inventory.save_products()
        elif option == "8":
            program_running = False

if __name__ == "__main__":
    main()