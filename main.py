#import dependencies
from product_class import Product

#given a file with products (comma delimited)
#ex - CH1,Chai,3.11
#build the products and return them as a list of objects
def build_products(in_file):

        #create a list to hold the created objects
        product_list = []

        #read in the first line
        product = in_file.readline()
        try:
            #read in all the products until we hit the end
            while product != "":
                #split the string into a list of elements
                # [prod_id, prod_name, prod_price]
                product_details = product.split(",")

                #only attempt to create an object if there are three elements in the list
                #exception will be thrown if the 3rd object is not a number 
                # ie - you can't have a string as a price
                if len(product_details) == 3:
                    prod_id = product_details[0]
                    prod_name = product_details[1]
                    prod_price = float(product_details[2])
                    product_list.append(Product(prod_id, \
                                                prod_name, \
                                                prod_price))
                    #print("Item Created: " + str(prod_id))
                
                #read in the next line from the file
                product = in_file.readline()
        #general exception handling
        except Exception as err:
            print("Error found!: ", err)
            print()
        #return the valid objects to main
        return product_list

            

def print_menu(product_list):
    print("+   ", "", "", "", "+", sep="\t")
    print("|","TODAY'S PRODUCTS","|", sep ="\t")
    print("+   ","---","---","---","+", sep = "\t")
    print("|","Code","Name","Price","|", sep = "\t")
    print("+   ", "---", "---", "---", "+", sep="\t")
    for product in product_list:
        print("|",str(product.code),str(product.name),"$"+str(product.price),"|", sep = "\t")
    print("+   ", "---", "---", "---", "+", sep="\t")
    print()


def print_commands():
    print("")

def take_command(command):



    



def main():
    product_file = open('product_input.txt', 'r')

    products = build_products(product_file)
    print_menu(products)











if __name__ == '__main__':
  main()
