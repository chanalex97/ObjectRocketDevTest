


class Promotions(object):
    def __init__(self):
        #flags for whether or not a discount has been applied
        #mainly useful for when discounts may only be applied once per cart
        self.is_bogo_used = False
        self.is_appl_used = False
        self.is_chmk_used = False
        self.is_apom_used = False



    #reset the flags when a new cart is created
    # def reset_promotions(self):
    #     self.is_bogo_used = False
    #     self.is_appl_used = False
    #     self.is_chmk_used = False
    #     self.is_apom_used = False



    #INPUT: Cart object
    #OUTPUT: NONE - discounts are applied to the qualifying products
    def is_bogo(self,current_order):
        #flag that states whether or not the the current coffee is free
        free_coffee = False
        #iterate through the cart object (object that holds other product objects)
        for product in current_order.cart:
            #if the product name is coffee, add it to the list, else pass
            #and make sure the product doesn't have the discount applied yet
            if (product.code == "CF1") and free_coffee and (product.discount.get('BOGO') == None):
                product.discount['BOGO'] = product.price * -1
                #reset the flag since we've applied the discount
                free_coffee = False
            #mark the next coffee as eligible
            elif product.code == "CF1" and not free_coffee:
                free_coffee = True

    #INPUT: Cart object
    #OUTPUT: NONE - discounts are applied to the qualifying products
    def is_appl(self, current_order):
        #create list to hold apple objects
        apple_list = []
        #iterate through the cart, and save the apple objects to apple_list
        for product in current_order.cart:
            if product.code == "AP1":
                apple_list.append(product)
        #if user has 3 or more apples, iterate through apple_list
        #apply the APPL discount to those that do not already have it
        if len(apple_list) >= 3:
            for product in apple_list:
                if product.discount.get('APPL') == None:
                    product.discount['APPL'] = float(-1.50)

    #INPUT: Cart object
    #OUTPUT: NONE - discounts are applied to the qualifying products
    def is_chmk(self, current_order):
        #if the discount has already been used, exit the function
        if not self.is_chmk_used:
            #list to hold product codes
            product_codes = []
            #collect all the product codes and save in product_codes
            for product in current_order.cart:
                product_codes.append(product.code)
            #if both chai and milk are in the cart
            #look for a milk to apply the discount to
            if ("CH1" in product_codes) and ("MK1" in product_codes):
                for product in current_order.cart:
                    # double check that the milk doesn't already have the discount applied
                    if (product.code == "MK1") and (product.discount.get('CHMK') == None):
                        product.discount['CHMK'] = product.price * -1
                        #set the discount as used
                        self.is_chmk_used = True
                        #exit out of the loop
                        break
            
    #INPUT: Cart object
    #OUTPUT: NONE - discounts are applied to the qualifying products
    def is_apom(self, current_order):
        #if the discount has already been used, exit the function
        if not self.is_apom_used:
            #list to hold product codes
            product_codes = []
            #collect all the product codes and save in product_codes
            for product in current_order.cart:
                product_codes.append(product.code)
            #if both oatmeal and apples are in the cart
            #look for a bag of apples to apply the discount to
            if ("AP1" in product_codes) and ("OM1" in product_codes):
                for product in current_order.cart:
                    if product.code == "AP1" and product.discount.get('APOM') == None:
                        # double check that the bag doesn't already have the discount applied
                        product.discount['APOM'] = product.price * -0.50
                        #set the discount as used
                        self.is_apom_used = True
                        #exit out of the loop
                        break

