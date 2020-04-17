import unittest
from lost_hat_add_to_basket_tests import LostHatBasketTests
from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_login_tests import LostHatLoginTests
from lost_hat_front_page_tests import LostHatFrontPageTests
from lost_hat_product_tests import LostHatProductTests


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatLoginTests))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductTests))
    test_suite.addTest(unittest.makeSuite(LostHatBasketTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())

