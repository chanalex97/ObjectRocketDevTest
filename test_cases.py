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

        #cart object instantiation
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

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_bogo(cart)
        #verify that the correct products are adjusted
        self.assertEqual(coffee1.discount.get("BOGO"), None)
        self.assertEqual(list(coffee2.discount.keys())[0], "BOGO")
        self.assertEqual(coffee3.discount.get("BOGO"), None)
        self.assertEqual(list(coffee4.discount.keys())[0], "BOGO")
        self.assertEqual(apple1.discount.get("BOGO"), None)
        #make sure the discount prices are correct
        self.assertEqual(coffee2.discount.get("BOGO"), coffee2.price * -1)
        self.assertEqual(coffee4.discount.get("BOGO"), coffee4.price * -1)


    #test is to make sure that given 4 apples and 1 oatmeal (APPL and APOM discounts applied),
    #3 of the apples will be $4.50 and the 4th will be $3.00, Oatmeal unchanged
    def test_appl_apom_3discounted_1halfoff(self):
        #instantiate products
        apple1 = Product("AP1", "Apples", 6.00)
        apple2 = Product("AP1", "Apples", 6.00)
        apple3 = Product("AP1", "Apples", 6.00)
        apple4 = Product("AP1", "Apples", 6.00)
        oatmeal1 = Product("OM1", "Oatmeal", 3.69)

        #make sure the products are actually Product objects
        self.assertIsInstance(apple1, Product)
        self.assertIsInstance(apple2, Product)
        self.assertIsInstance(apple3, Product)
        self.assertIsInstance(apple4, Product)
        self.assertIsInstance(oatmeal1, Product)

        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(apple1)
        cart.add_to_cart(apple2)
        cart.add_to_cart(apple3)
        cart.add_to_cart(apple4)
        cart.add_to_cart(oatmeal1)

        #make sure no preexisting APPL or APOM deals exist in the products
        self.assertEqual(apple1.discount.get("APPL"), None)
        self.assertEqual(apple1.discount.get("APOM"), None)
        self.assertEqual(apple2.discount.get("APPL"), None)
        self.assertEqual(apple1.discount.get("APOM"), None)
        self.assertEqual(apple3.discount.get("APPL"), None)
        self.assertEqual(apple1.discount.get("APOM"), None)
        self.assertEqual(apple4.discount.get("APPL"), None)
        self.assertEqual(oatmeal1.discount.get("APPL"), None)
        self.assertEqual(oatmeal1.discount.get("APOM"), None)

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_appl(cart)
        promos.is_apom(cart)

        #verify that the correct products are adjusted
        #only the first apple should have both discounts, the other 3 shouldn't
        self.assertDictContainsSubset(apple1.discount, {'APPL':-1.50,'APOM':apple1.price * -0.50})

        self.assertDictContainsSubset(apple2.discount, {'APPL': -1.50})
        self.assertEqual(apple2.discount.get('APOM'), None)

        self.assertDictContainsSubset(apple3.discount, {'APPL': -1.50})
        self.assertEqual(apple3.discount.get('APOM'), None)

        self.assertDictContainsSubset(apple4.discount, {'APPL': -1.50})
        self.assertEqual(apple4.discount.get('APOM'), None)

        #oatmeal remains unchanged
        self.assertEqual(oatmeal1.discount.get('APPL'), None)
        self.assertEqual(oatmeal1.discount.get('APOM'), None)

        #set the best discounts for each of the products
        for product in cart.cart:
            product.set_greatest_discount()
        #check that the best discounts are correct
        self.assertDictContainsSubset(apple1.best_discount, {'APOM': apple1.price * -0.50})
        self.assertDictContainsSubset(apple2.best_discount, {'APPL': -1.50})
        self.assertDictContainsSubset(apple3.best_discount, {'APPL': -1.50})
        self.assertDictContainsSubset(apple4.best_discount, {'APPL': -1.50})
        #oatmeal has no discounts
        self.assertEqual(len(oatmeal1.discount.keys()), 0)

    #test is to make sure that given 2 oatmeals and 2 chais (CHMK discount),
    #the CHMK discount will only be used once (applied on 1 milk, not both)
    def test_chmk(self):
        #instantiate the products
        chai1 = Product("CH1", "Chai", 3.11)
        chai2 = Product("CH1", "Chai", 3.11)
        milk1 = Product("MK1", "Milk", 4.75)
        milk2 = Product("MK1", "Milk", 4.75)

        #make sure they are type Product
        self.assertIsInstance(chai1, Product)
        self.assertIsInstance(chai2, Product)
        self.assertIsInstance(milk1, Product)
        self.assertIsInstance(milk2, Product)

        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(chai1)
        cart.add_to_cart(chai2)
        cart.add_to_cart(milk1)
        cart.add_to_cart(milk2)

        #make sure no preexisting CHMK deal exists in the products
        self.assertEqual(chai1.discount.get("CHMK"), None)
        self.assertEqual(chai2.discount.get("CHMK"), None)
        self.assertEqual(milk1.discount.get("CHMK"), None)
        self.assertEqual(milk2.discount.get("CHMK"), None)

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_chmk(cart)

        #verify that the correct products are adjusted
        self.assertDictContainsSubset(milk1.discount, {'CHMK': milk1.price * -1})
        self.assertEqual(milk2.discount.get('CHMK'), None)
        self.assertEqual(chai1.discount.get('CHMK'), None)
        self.assertEqual(chai2.discount.get('CHMK'), None)


##################
# CHECKOUT TESTS #
##################
class checkout_tests(TestCase):
    def test_ch_ap_cf_mk(self):
        apple = Product("AP1", "Apples", 6.00)
        coffee = Product("CF1", "Coffee", 11.23)
        chai = Product("CH1", "Chai", 3.11)
        milk = Product("MK1", "Milk", 4.75)

        self.assertIsInstance(apple, Product)
        self.assertIsInstance(coffee, Product)
        self.assertIsInstance(chai, Product)
        self.assertIsInstance(milk, Product)

        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(apple)
        cart.add_to_cart(chai)
        cart.add_to_cart(coffee)
        cart.add_to_cart(milk)

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_bogo(cart)
        promos.is_appl(cart)
        promos.is_chmk(cart)
        promos.is_apom(cart)

        cart.checkout()
        self.assertEqual(cart.total, 20.34)


    def test_ap_mk(self):
        apple = Product("AP1", "Apples", 6.00)
        milk = Product("MK1", "Milk", 4.75)

        self.assertIsInstance(apple, Product)
        self.assertIsInstance(milk, Product)

        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(apple)
        cart.add_to_cart(milk)

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_bogo(cart)
        promos.is_appl(cart)
        promos.is_chmk(cart)
        promos.is_apom(cart)

        cart.checkout()
        self.assertEqual(cart.total, 10.75)


    def test_cf_cf(self):
        coffee1 = Product("CF1", "Coffee", 11.23)
        coffee2 = Product("CF1", "Coffee", 11.23)

        self.assertIsInstance(coffee1, Product)
        self.assertIsInstance(coffee2, Product)


        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(coffee1)
        cart.add_to_cart(coffee2)


        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_bogo(cart)
        promos.is_appl(cart)
        promos.is_chmk(cart)
        promos.is_apom(cart)

        cart.checkout()
        self.assertEqual(cart.total, 11.23)

    def test_ap_ap_ch_ap(self):
        apple1 = Product("AP1", "Apples", 6.00)
        apple2 = Product("AP1", "Apples", 6.00)
        chai = Product("CH1", "Chai", 3.11)
        apple3 = Product("AP1", "Apples", 6.00)

        self.assertIsInstance(apple1, Product)
        self.assertIsInstance(apple2, Product)
        self.assertIsInstance(chai, Product)
        self.assertIsInstance(apple3, Product)

        #cart object instantiation
        cart = Cart()
        self.assertIsInstance(cart, Cart)

        #add items to the cart
        cart.add_to_cart(apple1)
        cart.add_to_cart(apple2)
        cart.add_to_cart(chai)
        cart.add_to_cart(apple3)

        #promotions
        promos = Promotions()
        #apply the promotion rules to the cart
        promos.is_bogo(cart)
        promos.is_appl(cart)
        promos.is_chmk(cart)
        promos.is_apom(cart)

        cart.checkout()
        self.assertEqual(cart.total, 16.61)

if __name__ == '__main__':
    main()
