#import dependencies
from product_class import Product
from cart_class import Cart
from promotions_class import Promotions

#INPUT: A file with products (comma delimited)
    #ex - CH1,Chai,3.11
#OUTPUT: Return list of product objects
def build_products(in_file):

        #create a list to hold the created objects
        product_list = []

        #read in the first line
        product = in_file.readline()
        try:
            #read in all the products until we hit the end
            while product != "":
                #split the string into a list of elements
                # [prod_code, prod_name, prod_price]
                product_details = product.split(",")

                #only attempt to create an object if there are three elements in the list
                #exception will be thrown if the 3rd object is not a number 
                # ie - you can't have a string as a price
                if len(product_details) == 3:
                    prod_code = product_details[0]
                    prod_name = product_details[1]
                    prod_price = float(product_details[2])
                    product_list.append(Product(prod_code, prod_name, prod_price))
                
                #read in the next line from the file
                product = in_file.readline()
        #general exception handling
        except Exception as err:
            print("Error found!: ", err)
            print()
        #return the valid objects to main
        return product_list

            
#INPUT: Product list
#OUTPUT: Displays product menu
def print_menu(product_list):
    #print the product menu
    print("+   ", "", "", "", "+", sep="\t")
    print("|","TODAY'S PRODUCTS","|", sep ="\t")
    print("+   ","---","---","---","+", sep = "\t")
    print("|","Code","Name","Price","|", sep = "\t")
    print("+   ", "---", "---", "---", "+", sep="\t")
    
    #iterate through the list of product objects
    for product in product_list:
        print("|",str(product.code),str(product.name),"$"+format((product.price),'.2f'),"|", sep = "\t")
    print("+   ", "---", "---", "---", "+", sep="\t")
    print()


#INPUT: NONE
#OUTPUT: Display List of user commands
def print_commands():
    #print the choice menu
    print("+   ", "", "", "", "", "+", sep="\t")
    print("|", "USER COMMANDS", "","","|", sep="\t")
    print("+   ", "---", "---", "---", "---", "+", sep="\t")
    print("|", "Option 1: Add Item to Cart", "|", sep="\t")
    print("|", "Option 2: View Cart", "", "|", sep="\t")
    print("|", "Option 3: Checkout", "", "|", sep="\t")
    print("+   ", "---", "---", "---", "---", "+", sep="\t")


#INPUT: NONE
#OUTPUT: Return user command choice
def take_command():
    #call the print_commands functions to show the commands options
    print_commands()
    #ask user for choice
    choice = input("\nEnter your choice (1, 2, or 3): ")
    #validate that it is a correct choice
    #if not, continue prompting until a correct choice is entered
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid Choice. Enter your choice (1, 2,or 3): ")

    #return the choice as an integer
    return int(choice)


#INPUT: Product list
#OUTPUT: Calls a function to create the object given the product code, and returns the object
def request_item_for_cart(product_list):
    #collect a list of product codes
    prod_code_list = [product.code for product in product_list]

    #ask for user input
    product_code = input("Enter your desired product code: ")
    #convert input letters to uppercase
    product_code = product_code.upper()
    #validate that it is a valid product code
    while product_code not in prod_code_list:
        product_code = input("Invalid! Enter your desired product code: ")
        #convert input letters to uppercase
        product_code = product_code.upper()

    return make_cart_item(product_code, product_list)


#this next function is necessary because we don't want to overwrite the attributes of the original product
#instead, we want to create a duplicate, so when we add discount features or make any adjustments, it doesn't affect the original object

#INPUT: Product code, product list
#OUTPUT: return an instantiation for Product to request_item_for_cart
def make_cart_item(code, product_list):
    for product in product_list:
        if product.code == code:
            return Product(code, product.name, product.price)


    



def main():
    #set a pointer to the file
    product_file = open('product_input.txt', 'r')

    #build the list of available products
    products = build_products(product_file)

    #print the Product Menu
    print_menu(products)

    #declare an empty cart
    cart = Cart()

    #take in a user command
    user_choice = take_command()

    #flag that continues the program until the user requests to stop
    interaction_flag = 99

    #create a promotions object
    promos = Promotions()

    #continue program until checkout occurs
    while interaction_flag != -1:
        #Add item to cart
        if user_choice == 1:
            #request user to enter item, and if valid, add to cart
            cart.add_to_cart(request_item_for_cart(products))
            print("Product Added!\n")

            #take another command
            user_choice = take_command()
        #View Cart
        elif user_choice == 2:
            #run all the items in the cart though each of the promotions
            promos.is_bogo(cart)
            promos.is_appl(cart)
            promos.is_chmk(cart)
            promos.is_apom(cart)
            #view cart
            cart.view_cart()

            #take another command
            user_choice = take_command()
        #Checkout
        elif user_choice == 3:
            #call checkout function
            cart.checkout()
            #change flag to end program
            interaction_flag = -1
            print("Thanks for shopping with us!")


if __name__ == '__main__':
  main()
