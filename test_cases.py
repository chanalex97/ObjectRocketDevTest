from unittest import main, TestCase
from product_class import Product
from cart_class import Cart
from promotions_class import Promotions


#######################
# PRODUCT CLASS TESTS #
#######################
class product_class_tests(TestCase):
    #best case of how data types should be
    def test_base(self):
        apple = Product("AP1", "Apples", 6.00)
        self.assertIsInstance(apple, Product)
        self.assertEqual(apple.code, "AP1" )
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    #even if price is saved as a string, it shouldn't affect the product
    def test_price_as_string(self):
        apple = Product("AP1", "Apples", "6.00")
        self.assertIsInstance(apple, Product)
        self.assertEqual(apple.code, "AP1")
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    #check if having code as a number will be converted correctly
    def test_code_as_int(self):
        apple = Product(111, "Apples", 6.00)
        self.assertIsInstance(apple, Product)
        self.assertEqual(apple.code, "111")
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    #check if having code as a number will be converted correctly
    def test_name_as_int(self):
        apple = Product("AP1", 111, 6.00)
        self.assertIsInstance(apple, Product)
        self.assertEqual(apple.code, "AP1")
        self.assertEqual(apple.name, "111")
        self.assertEqual(apple.price, 6.00)
    
    def test_set_best_discount(self):
        apple = Product("AP1", "Apples", 6.00)
        self.assertIsInstance(apple, Product)
        apple.discount['BOGO'] = apple.price * - 1
        apple.discount['APOM'] = apple.price * - 0.5
        apple.set_greatest_discount()
        self.assertEqual(list(apple.best_discount.keys())[0], "BOGO")
        self.assertEqual(list(apple.best_discount.values())[0], -6.00)
        self.assertEqual(apple.greatest_discount_price, -6.00)


#####################
# CART CLASS TESTS #
#####################
class cart_class_tests(TestCase):
    def test_correct_item(self):
        cart = Cart()
        false_item = [1, 2, 3]
        self.assertNotIsInstance(false_item, Product)
        self.assertRaises(TypeError, cart.add_to_cart(false_item))


#########################
# PROMOTION CLASS TESTS #
#########################
class promotion_class_tests(TestCase):
    #instantiate objects that will be used for promotion test cases

    #products

    apple2 = Product("AP1", "Apples", 6.00)
    apple3 = Product("AP1", "Apples", 6.00)


    chai1 = Product("CH1", "Chai", 3.11)
    chai2 = Product("CH1", "Chai", 3.11)

    milk1 = Product("MK1", "Milk", 4.75)
    milk2 = Product("MK1", "Milk", 4.75)

    oatmeal1 = Product("OM1", "Oatmeal", 3.69)
    oatmeal2 = Product("OM1", "Oatmeal", 3.69)

    def test_product_types(self):
        #make sure products are actually products

        self.assertIsInstance(self.apple2, Product)
        self.assertIsInstance(self.apple3, Product)



        self.assertIsInstance(self.chai1, Product)
        self.assertIsInstance(self.chai2, Product)

        self.assertIsInstance(self.milk1, Product)
        self.assertIsInstance(self.milk2, Product)

        self.assertIsInstance(self.oatmeal1, Product)
        self.assertIsInstance(self.oatmeal2, Product)

    #promotions
    promos = Promotions()

    #test is to make sure that given 4 coffees,
    #2 are discounted and 2 are not
    #a non-coffee product is added to make sure non-coffee products aren't changed
    def test_bogo_2reg_2free(self):
        #instantiate products
        apple1 = Product("AP1", "Apples", 6.00)
        coffee1 = Product("CF1", "Coffee", 11.23)
        coffee2 = Product("CF1", "Coffee", 11.23)
        coffee3 = Product("CF1", "Coffee", 11.23)
        coffee4 = Product("CF1", "Coffee", 11.23)

        #make sure the products are actually Product objects
        self.assertIsInstance(apple1, Product)
        self.assertIsInstance(coffee1, Product)
        self.assertIsInstance(coffee2, Product)
        self.assertIsInstance(coffee3, Product)
        self.assertIsInstance(coffee4, Product)

        #cart object instantiaion
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(coffee1)
        cart.add_to_cart(coffee2)
        cart.add_to_cart(coffee3)
        cart.add_to_cart(coffee4)
        cart.add_to_cart(apple1)

        #make sure no preexisting bogo deals exist in the products
        self.assertEqual(coffee1.discount.get("BOGO"), None)
        self.assertEqual(coffee2.discount.get("BOGO"), None)
        self.assertEqual(coffee3.discount.get("BOGO"), None)
        self.assertEqual(coffee4.discount.get("BOGO"), None)
        self.assertEqual(apple1.discount.get("BOGO"), None)
        #apply the promotion rules to the cart
        self.promos.is_bogo(cart)
        #verify that the correct products are adjusted
        self.assertEqual(coffee1.discount.get("BOGO"), None)
        self.assertEqual(list(coffee2.discount.keys())[0], "BOGO")
        self.assertEqual(coffee3.discount.get("BOGO"), None)
        self.assertEqual(list(coffee4.discount.keys())[0], "BOGO")
        self.assertEqual(apple1.discount.get("BOGO"), None)
        #make sure the discount prices are correct
        self.assertEqual(coffee2.discount.get("BOGO"), coffee2.price * -1)
        self.assertEqual(coffee4.discount.get("BOGO"), coffee4.price * -1)






if __name__ == '__main__':
    main()
