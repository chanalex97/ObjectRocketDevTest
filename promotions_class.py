


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
            #if the product name is coffee, add it to the list, else pass
            if product.code == "CF1" and free_coffee:
                if product.discount.get('BOGO') == None:
                    product.discount['BOGO'] = product.price * -1
                free_coffee = False
            elif product.code == "CF1" and not free_coffee:
                free_coffee = True

    def is_appl(self, current_order):

        apple_list = []

        for product in current_order.cart:
            if product.code == "AP1":
                apple_list.append(product)
        if len(apple_list) >= 3:
            for product in apple_list:
                if product.discount.get('APPL') == None:
                    product.discount['APPL'] = product.price - 1.50

    def is_chmk(self, current_order):
        if self.is_chmk_used:
            pass
        else:
            product_codes = []
            for product in current_order:
                product_codes.append(product.code)
            if ("CH1" in product_codes) and ("MK1" in product_codes):
                for product in current_order:
                    if product.code == "MK1":
                        if product.discount.get('CHMK') == None:
                            product.discount['CHMK'] = product.price * -1
                            self.is_chmk_used = True
                            break
            


    def is_apom(self, current_order):
        pass

    def find_promotions(self, current_order):
        pass

