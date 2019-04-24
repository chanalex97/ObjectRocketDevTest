


class Promotions():
    def __init__(self, cart):
        self.cart = cart
    
    def is_bogo(self,cart):

        #create a list to store only the coffee objects
        coffees = []

        #iterate through the cart object (object that holds other product objects)
        for product in cart:
            #if the product name is coffee, add it to the list, else pass
            if product.name == "CF1":
                coffees.append(product)
        

    def is_appl(self,cart):
        pass
    def is_chmk(self,cart):
        pass
    def is_apom(self,cart):
        pass
    def find_promotions(self,cart):
        pass

