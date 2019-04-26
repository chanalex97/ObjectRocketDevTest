


class Promotions(object):
    def __init__(self):

        self.is_bogo_used = False
        self.is_appl_used = False
        self.is_chmk_used = False
        self.is_apom_used = False

    #INPUT: Cart object
    #OUTPUT: NONE - discounts are applied to the qualifying products
    def is_bogo(self,current_order):

        #flag that states whether or not the the current coffee is free
        free_coffee = False

        #iterate through the cart object (object that holds other product objects)
        for product in current_order.cart:
            print(product)
            #if the product name is coffee, add it to the list, else pass
            if product.code == "CF1" and free_coffee:
                if product.discount.get('BOGO') == None:
                    product.discount['BOGO'] = product.price * -1
                    print(product.discount.keys())
                    print(product.discount.values())
                    print(product.discount['BOGO'])

                free_coffee = False
            elif product.code == "CF1" and not free_coffee:
                free_coffee = True


    def is_appl(self,cart):
        pass
    def is_chmk(self,cart):
        pass
    def is_apom(self,cart):
        pass
    def find_promotions(self,cart):
        pass

