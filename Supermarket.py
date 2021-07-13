# General Variable Defines.
summary = 0
shopping_list = []
isShopping = True
print("Welcome to the best market in town Davidtheking's supermarket", end="")

# Loop of shopping as long as the user don't enter 3 he will keep shopping.
while isShopping:
    # Main Menu show up
    print("\nHere's the Main Menu for you:\n"
          "Chose 1 - To add to the Cart\n"
          "Chose 2 - To remove from the Cart\n"
          "Chose 3 - To stop Shopping\n")
    choice = input("Please enter your choice: ")

    # Variables that will help us define the item dictionary.
    product = {}
    sub_product = {}

    if choice == '1':  # Choice one for get a new item for the list.
        product_name = input("Please enter the product name you would like to add: ")
        product_cost = input("Please enter the product cost value: ")
        product_quantity = input("Please enter how much %s you want to buy: " % product_name)
        if not shopping_list:  # Check if the list empty.
            sub_product[product_cost] = product_quantity
            product[product_name] = sub_product
            shopping_list.append(product)
        else:  # If the list isn't empty check if the item is exist already.
            isExist = False
            for item in shopping_list:
                if product_name in item:
                    old_quantity = int(list(item[product_name].values())[0])
                    sub_product[product_cost] = old_quantity + int(product_quantity)
                    product[product_name] = sub_product
                    shopping_list.remove(item)
                    shopping_list.append(product)
                    isExist = True
            if not isExist:  # If the item isn't exist add it.
                sub_product[product_cost] = product_quantity
                product[product_name] = sub_product
                shopping_list.append(product)
    elif choice == '2':  # Choice two for remove item from the list.
        product_name = input("Please enter the product name you would like to remove: ")
        product_quantity = int(input("Please enter how much %s you want to remove: " % product_name))
        if not shopping_list:  # Check if the list empty.
            print("You cannot remove from the cart if there is no cart ;)")
        else:  # If the list isn't empty check if the item is exist already.
            isExist = False
            for item in shopping_list:
                if product_name in item:
                    old_quantity = int(list(item[product_name].values())[0])
                    product_cost = list(item[list(item)[0]])[0]
                    if old_quantity > product_quantity:  # Check if there is enough from the item or remove it all.
                        sub_product[product_cost] = old_quantity - int(product_quantity)
                        product[product_name] = sub_product
                        shopping_list.remove(item)
                        shopping_list.append(product)
                    else:
                        shopping_list.remove(item)
                    isExist = True
            if not isExist:  # If the item isn't exist we can't remove it.
                print("\nProduct %s doesn't exist in your cart." % product_name)
    elif choice == '3':  # Choice three for printing the receipt.
        for item in shopping_list:  # Print a nice receipt for the customer.
            item_name = list(item)[0]
            item_cost = int(list(item[list(item)[0]])[0])
            item_quantity = int(item[list(item)[0]][list(item[list(item)[0]])[0]])
            total = item_cost * item_quantity
            print(item_name, "                     price", item_cost)
            print("X", item_quantity, "             total price", total)
            summary += total  # Calculate the total cost.
        print("\nYour total bill amount is %d.\n" % summary)
        isShopping = False
    else:
        print("Please choose a number only form the menu options.")

print("Thanks for visiting at Davidtheking's supermarket\n"
      "Have a good rest of the day.")
