

#create a generic product class
#based on specs, a product has 3 attributes
#   1. Product Code
#   2. Name
#   3. Price
class Product(object):
    def __init__(self,product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price

    #return string method that shows the attributes for the object
    def __str__(self):
        return "Product code: " + str(self.product_code) + "\nName: " + str(self.name) + "\nPrice: " + str(self.price)