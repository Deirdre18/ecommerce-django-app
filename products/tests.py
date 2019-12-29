from django.test import TestCase
from .models import Product

# Create your tests here.
# try to think of other things to test??
# creating product test which inherits from test case.


class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model. In order to run tests, 'test' must be defined at start.
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'An product')
