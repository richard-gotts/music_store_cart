"""
This is a shopping cart application for customers at the fictional music supplies shop 'The Music
Store'. The app allows customers to:

    - View a list of available products
    - Add or remove items from their cart
    - View the total cost of their cart
    - Checkout (closes the application)

"""

# Dictionary of products and their prices
product_prices = {"Drum brushes": 12.99,
                  "Drumsticks": 4.49,
                  "Electric guitar strings": 5.49,
                  "Guitar tuner": 9.99,
                  "Headphones": 34.99,
                  "Manuscript paper": 5.99,
                  "Metronome": 21.99,
                  "Microphone": 32.29,
                  "Music stand": 21.99,
                  "Music stand light": 30.99,
                  "Piano stool": 17.99,
                  "Plectrums (x20)": 3.99,
                  "Sheet music clips (x4)": 5.19}

# Initialise 'checked out' boolean
CHECKED_OUT = False

# Generate another dictionary to store the quantity of each product along with its price
user_cart = {product: [product_prices.get(product), 0] for product in product_prices}

def store_heading():
    """Prints a heading for The Music Store"""
    print("\n" + "_" * 100 + "\n\033[1m" + "The Music Store\n" + "\033[0m")

def sum_cart():
    """Calculates the total cost of the cart"""
    cart_total = 0
    for product in user_cart:
        product_total = user_cart.get(product)[0] * user_cart.get(product)[1]
        cart_total += product_total
    return cart_total

def cart_empty_check():
    """Returns True if the cart is empty and False if there is anything in the cart"""
    cart_empty = True
    for product in user_cart:
        if user_cart.get(product)[1] != 0:
            cart_empty = False
            break
    return cart_empty

def show_cart():
    """If there is anything in the cart, the contents of the cart with quantities greater than zero
    are printed. The products are printed alongside their quantity and cost for that quantity."""
    cart_empty = cart_empty_check()
    if not cart_empty:
        print("- " * 50 + f"\nYOUR CART (£{sum_cart():.2f})\n")
        print("\033[1m" + "Product" + " " * 18 + "Quantity  Cost" + "\033[0m")
        for product in user_cart:
            if user_cart.get(product)[1] != 0:
                product_total = user_cart.get(product)[0] * user_cart.get(product)[1]
                print(product + " " * (25 - len(product)) + str(user_cart.get(product)[1]) + " " * \
                      (10 - len(str(user_cart.get(product)[1]))) + f"£{product_total:.2f}")
            else:
                pass
        print("\n" + "- " * 50 + "\n")
    else:
        pass

def product_list():
    """Prints a numbered list of available products"""
    for pos, product in enumerate(product_prices):
        if pos < 9:
            print(str(pos + 1) + ". " + product + " " * (25 - len(product)) + \
                  f"£{product_prices.get(product)}")
        else:
            print(str(pos + 1) + "." + product + " " * (25 - len(product)) + \
                  f"£{product_prices.get(product)}")

def main_menu():
    """Prints the store heading and cart, as well as a set of options for the user to choose from.
    Invalid user inputs raise an error message and the user is prompted to try again. If the cart is
    empty, 'remove' and 'checkout' options are invalid. Returns the user's chosen option."""
    store_heading()
    show_cart()
    print("'v' - view available products\n'a' - add products to your cart\n'r' - remove products "
          "from your cart\n'c' - checkout\n")
    cart_empty = cart_empty_check()
    valid_option = False
    user_option = input("To select an option, please type the corresponding letter: ").lower()
    while not valid_option:
        while user_option not in ["v", "a", "r", "c"]:
            user_option = input("The letter you typed is not an option! Please try again: ").lower()
        while user_option in ["r", "c"] and cart_empty:
            user_option = input("Your cart is currently empty. Please choose another "
                                "option: ").lower()
        if user_option not in ["v", "a", "r", "c"]:
            continue
        valid_option = True
    return user_option

def view_menu():
    """Prints the store heading and cart, as well as a numbered list of avaliable products and a set
    of options for the user to choose from. Invalid user inputs raise an error message and the user 
    is prompted to try again. Returns the user's chosen option."""
    store_heading()
    show_cart()
    product_list()
    print("\n'a' - add products to your cart\n'm' - return to main menu\n")
    user_option = input("To select an option, please type the corresponding letter: ").lower()
    while user_option not in ["a", "m"]:
        user_option = input("The letter you typed is not an option! Please try again: ").lower()
    return user_option

def add_products():
    """As long as the user doesn't return to the main menu, an adding loop is executed:
    
    Prints the store heading and cart, as well as a numbered list of available products. The user
    can type a number to add the corresponding product and can select a quantity of that product to
    be added. Invalid user inputs raise an error message and the user is prompted to try again. The
    cart is updated with the products added by the user and their quantities."""
    finished_adding = False
    while not finished_adding:
        store_heading()
        show_cart()
        product_list()
        user_option = input("\nTo add a product to your cart, please type the corresponding "
                            "number or type 'm' to return to the \nmain menu: ").lower()
        while user_option not in [str(num) for num in range(1, len(product_prices) + 1)] + ["m"]:
            user_option = input("The number/letter you typed is not an option! Please try "
                                "again: ").lower()
        if user_option == "m":
            finished_adding = True
        else:
            product_quantity = input("Please select the quantity for this product: ")
            while not product_quantity.isnumeric():
                product_quantity = input("The quantity must be a whole number! Please try again: ")
            product_quantity = int(product_quantity)
            if product_quantity == 0:
                print("\nNo items were added to your cart.")
            else:
                for pos, product in enumerate(product_prices):
                    if pos == int(user_option) - 1:
                        user_cart.get(product)[1] += product_quantity
                    else:
                        pass
                if product_quantity == 1:
                    print(f"\n{product_quantity} item was added to your cart.")
                else:
                    print(f"\n{product_quantity} items were added to your cart.")

def remove_products():
    """As long as the cart isn't empty and the user doesn't return to the main menu, a removing loop
    is executed:
    
    Prints the store heading and cart, and prints a numbered list of products in the cart with
    quantities greater than zero and their respective quantities. The user can type a number to
    remove the corresponding product and can select a quantity of that product to remove. Invalid
    user inputs raise an error message and the user is prompted to try again. The cart is
    updated."""
    finished_removing = False
    cart_empty = cart_empty_check()
    while not cart_empty and not finished_removing:
        store_heading()
        show_cart()
        removal_list = []
        for product in user_cart:
            if user_cart.get(product)[1] != 0:
                removal_list.append([product, user_cart.get(product)[1]])
            else:
                pass
        for pos, product in enumerate(removal_list):
            if pos < 9:
                print(str(pos + 1) + ". " + product[0] + " " * (25 - len(product[0])) + \
                      f"[{product[1]}]")
            else:
                print(str(pos + 1) + "." + product[0] + " " * (25 - len(product[0])) + \
                      f"[{product[1]}]")
        user_option = input("\nTo remove a product from your cart, please type the corresponding "
                            "number or type 'm' to return to \nthe main menu: ").lower()
        while user_option not in [str(num) for num in range(1, len(removal_list) + 1)] + ["m"]:
            user_option = input("The number/letter you typed is not an option! Please try "
                                "again: ").lower()
        if user_option == "m":
            finished_removing = True
        else:
            removal_quantity = input("How many items of this product would you like to remove? ")
            while not removal_quantity.isnumeric():
                removal_quantity = input("You must enter a whole number to remove! Please try "
                                         "again: ")
            removal_quantity = int(removal_quantity)
            if removal_quantity == 0:
                print("\nNo items were removed from your cart.")
            else:
                for pos, product in enumerate(removal_list):
                    if pos == int(user_option) - 1:
                        if removal_quantity <= product[1]:
                            user_cart.get(product[0])[1] -= removal_quantity
                            if removal_quantity == 1:
                                print(f"\n{removal_quantity} item was removed from your cart.")
                            else:
                                print(f"\n{removal_quantity} items were removed from your cart.")
                        else:
                            if user_cart.get(product[0])[1] == 1:
                                print(f"\n{user_cart.get(product[0])[1]} item was removed from "
                                      "your cart.")
                            else:
                                print(f"\n{user_cart.get(product[0])[1]} items were removed from "
                                      "your cart.")
                            user_cart.get(product[0])[1] = 0
                    else:
                        pass
        cart_empty = cart_empty_check()

def checkout_menu():
    """Prints the store heading and cart, as well options for the user to either checkout or
    return to the main menu. Invalid user input raises an error message and the user is prompted
    to try again. If the user checks out, True is returned, otherwise False is returned."""
    store_heading()
    show_cart()
    confirm_checkout = False
    print("Are you happy with your cart?\n\n'y' - yes, proceed to payment\n'n' - no, return me to "
          "the main menu\n")
    user_option = input("Please type 'y' or 'n' to proceed: ").lower()
    while user_option not in ["y", "n"]:
        user_option = input("The letter you typed is not an option! Please try again: ").lower()
    if user_option == "y":
        print("\nProceeding to payment...\n")
        confirm_checkout = True
    else:
        pass
    return confirm_checkout

# This loop controls the flow of the program and runs until the user checks out
while not CHECKED_OUT:
    user_choice = main_menu()
    if user_choice == "v":
        user_choice = view_menu()
        if user_choice == "a":
            add_products()
    elif user_choice == "a":
        add_products()
    elif user_choice == "r":
        remove_products()
    else:
        CHECKED_OUT = checkout_menu()
