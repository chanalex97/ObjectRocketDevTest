

#create a generic product class
#based on specs, a product has 3 attributes
#   1. Product Code
#   2. Name
#   3. Price
class Product(object):
    def __init__(self,code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.discount = {}
        self.greatest_discount_price = 0


    #return string method that shows the attributes for the object
    def __str__(self):
        # if self.discount_price == 0 and self.discount_name == "":
        #     return str(self.product_code) + "\t\t\t\t\t" + str(self.discount) + str(self.price)
        # if self.discount_price == 0:
        #     return str(self.product_code) + "\t\t\t\t\t" + str(self.discount) + str(self.price)
        return "Product code: " + str(self.code) + "\nName: " + str(self.name) + "\nPrice: " + str(self.price)