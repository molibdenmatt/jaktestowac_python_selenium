import unittest
from lost_hat_login_tests import LostHatLoginTests
from lost_hat_front_page_tests import LostHatFrontPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatLoginTests('test_logging_positive'))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())
