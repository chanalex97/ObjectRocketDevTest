

#create a generic product class
#based on specs, a product has 3 attributes
#   1. Product Code
#   2. Name
#   3. Price
class Product(object):
    def __init__(self,code, name, price):
        self.code = str(code)
        self.name = str(name)
        self.price = float(price)
        self.discount = {}
        self.best_discount = {}
        self.greatest_discount_price = 0

    #in the event that the product might be eligible for more than 1 discount
    #find the highest discount value, and use that for checkout

    #INPUT: None
    #OUTPUT: None - it just edit's the object's best_discount and greatest_discount price
    def set_greatest_discount(self):
        #see if the item has any discounts saved
        if len(self.discount.keys()) != 0:
            #iterate through all the discounts it has
            for discount, value in self.discount.items():
                #it's important to note that default is discount is 0
                #discounts are saved as negative numbers, and 0 is greater than any neg number
                if self.greatest_discount_price > value:
                    #set the new greatest discount price
                    self.greatest_discount_price = value
                    #clear the best_discount dictionary of any previous discounts
                    self.best_discount.clear()
                    #save the new "best" discount
                    self.best_discount[discount] = value

        


    #return string method that shows the attributes for the object, mainly used for debugging purposes
    def __str__(self):
        # if self.discount_price == 0 and self.discount_name == "":
        #     return str(self.product_code) + "\t\t\t\t\t" + str(self.discount) + str(self.price)
        # if self.discount_price == 0:
        #     return str(self.product_code) + "\t\t\t\t\t" + str(self.discount) + str(self.price)
        return "Product code: " + str(self.code) + "\nName: " + str(self.name) + "\nPrice: " + str(self.price)