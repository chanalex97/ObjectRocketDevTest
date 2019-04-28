


class Cart(object):
    def __init__(self):
        self.cart = []
        #used to denote when the cart is empty
        self.empty = True
        self.total = 0
    

    #INPUT: Product object
    #OUTPUT: None - add product to cart
    def add_to_cart(self, product):
        self.cart.append(product)
        #if this is the first item in the cart, change the state of the cart to not empty
        if self.empty == True:
            self.empty = False
    
    #INPUT: None
    #OUTPUT: Display the current items in cart, their discounts, and total price
    def view_cart(self):
        if not self.empty:
            #self.total could technically be a local variable "total" within this function alone
            #however, a variable is needed for reference during unit testing
            self.total = 0

            #set the best discounts for each object, applies the discount, 
            # and adds the difference to the total
            for product in self.cart:
                product.set_greatest_discount()
                self.total += product.price + product.greatest_discount_price

            #print the results
            print("+   ", "", "", "", "", "","", "+", sep="\t")
            print("|", "CURRENT CART", "", "", "","", "|", sep="\t")
            print("+   ", "", "", "", "", "", "", "+", sep="\t")
            print("|   ", "CODE", "NAME", "DISCOUNT", "PRICE", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            for product in self.cart:
                print("|", str(product.code), str(product.name), "", "",
                        "$"+format(product.price, ".2f"), "\t|", sep="\t")
                if len(product.best_discount.keys()) != 0:
                    for promo, disc_value in product.best_discount.items():
                        print("|", "", "", promo, "", format(disc_value, '.2f'), "", "|", sep= "\t")
                print("|   ", "", "", "", "", "", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print("|   ", "TOTAL:", "", "", "", "$"+format(self.total, ".2f"), "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print()
        else:
            print("Cart Empty")
        
    #INPUT: None
    #OUTPUT: Display the current items in cart, their discounts, and total price
    def checkout(self):
        if not self.empty:
            #self.total could technically be a local variable "total" within this function alone
            #however, a variable is needed for reference during unit testing
            self.total = 0

            #set the best discounts for each object, applies the discount,
            # and adds the difference to the total
            for product in self.cart:
                product.set_greatest_discount()
                self.total += product.price + product.greatest_discount_price

            #print the results
            print("+   ", "", "", "", "", "","", "+", sep="\t")
            print("|", "SALES RECEIPT", "", "", "","", "|", sep="\t")
            print("+   ", "", "", "", "", "", "", "+", sep="\t")
            print("|   ", "CODE", "NAME", "DISCOUNT", "PRICE", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            for product in self.cart:
                print("|", str(product.code), str(product.name), "", "",
                        "$"+format(product.price, ".2f"), "\t|", sep="\t")
                if len(product.best_discount.keys()) != 0:
                    for promo, disc_value in product.best_discount.items():
                        print("|", "", "", promo, "", format(disc_value, '.2f'), "", "|", sep= "\t")
                print("|   ", "", "", "", "", "", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print("|   ", "TOTAL:", "", "", "", "$"+format(self.total,".2f"), "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print()
        else:
            print("Cart Empty")




