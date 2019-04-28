from unittest import main, TestCase
from product_class import Product
from cart_class import Cart
from promotions_class import Promotions


class product_class_tests(TestCase):
    def base(self):
        apple = Product("AP1", "Apples", 6.00)
        self.assertEqual(apple.code, "AP1" )
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    def price_as_string(self):
        apple = Product("AP1", "Apples", "6.00")
        self.assertEqual(apple.code, "AP1")
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    def code_as_int(self):
        apple = Product(111, "Apples", 6.00)
        self.assertEqual(apple.code, "111")
        self.assertEqual(apple.name, "Apples")
        self.assertEqual(apple.price, 6.00)

    def name_as_int(self):
        apple = Product("AP1", 111, 6.00)
        self.assertEqual(apple.code, "AP1")
        self.assertEqual(apple.name, "111")
        self.assertEqual(apple.price, 6.00)


if __name__ == '__main__':
    main()
