


class Cart(object):
    def __init__(self):
        self.cart = []
        self.empty = True
    
    def is_empty(self, state):
        self.empty = state
    
    def empty_cart(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
    
    def view_cart(self):
        if len(self.cart) != 0:
            print("+   ", "", "", "", "", "+", sep="\t")
            print("|", "CURRENT CART", "", "", "|", sep="\t")

            for product in self.cart:
                print("|", str(product.code), str(product.name),
                        "$"+str(product.price), "\t|", sep="\t")

            print("+   ", "---", "---", "---", "\t+", sep="\t")
        else:
            print("Cart Empty")
        
            
    
    def checkout(self):
        pass
