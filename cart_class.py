


class Cart(object):
    def __init__(self):
        self.cart = []
        self.empty = True
    
    #used to denote when the cart is empty
    def is_empty(self, state):
        self.empty = state

    def reset_cart(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
    
    def view_cart(self):
        if not self.empty:

            #set the best discounts for each object
            for product in self.cart:
                product.set_greatest_discount()

            print("+   ", "", "", "", "", "","", "+", sep="\t")
            print("|", "CURRENT CART", "", "", "","", "|", sep="\t")
            print("+   ", "", "", "", "", "", "", "+", sep="\t")
            print("|   ", "CODE", "NAME", "DISCOUNT", "PRICE", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            for product in self.cart:
                print("|", str(product.code), str(product.name), "", "",
                        "$"+format(product.price, ".2f"), "\t|", sep="\t")

                # if len(product.discount.keys()) != 0:
                #     for promo, disc_value in product.discount.items():
                # print("|","","",promo, "", format(disc_value, '.2f'),"","|", sep = "\t")
                if len(product.best_discount.keys()) != 0:
                    for promo, disc_value in product.best_discount.items():
                        print("|", "", "", promo, "", format(disc_value, '.2f'), "", "|", sep= "\t")
                print("|   ", "", "", "", "", "", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")

            #create the total variable
            total = 0

            for product in self.cart:
                total += product.price + product.greatest_discount_price

            print("|   ", "TOTAL:", "", "", "", format(
                total, ".2f"), "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print()
        else:
            print("Cart Empty")
        
    
    def checkout(self):
        if not self.empty:

            #set the best discounts for each object
            for product in self.cart:
                product.set_greatest_discount()

            print("+   ", "", "", "", "", "","", "+", sep="\t")
            print("|", "SALES RECEIPT", "", "", "","", "|", sep="\t")
            print("+   ", "", "", "", "", "", "", "+", sep="\t")
            print("|   ", "CODE", "NAME", "DISCOUNT", "PRICE", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            for product in self.cart:
                print("|", str(product.code), str(product.name), "", "",
                        "$"+format(product.price, ".2f"), "\t|", sep="\t")

                # if len(product.discount.keys()) != 0:
                #     for promo, disc_value in product.discount.items():
                # print("|","","",promo, "", format(disc_value, '.2f'),"","|", sep = "\t")
                if len(product.best_discount.keys()) != 0:
                    for promo, disc_value in product.best_discount.items():
                        print("|", "", "", promo, "", format(disc_value, '.2f'), "", "|", sep= "\t")
                print("|   ", "", "", "", "", "", "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")

            #create the total variable
            total = 0

            for product in self.cart:
                total += product.price + product.greatest_discount_price

            print("|   ", "TOTAL:", "", "", "", format(total,".2f"), "\t|", sep="\t")
            print("+   ", "---", "---", "---", "", "---", "\t+", sep="\t")
            print()
        else:
            print("Cart Empty")




