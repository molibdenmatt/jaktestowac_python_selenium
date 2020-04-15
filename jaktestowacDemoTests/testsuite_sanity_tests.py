import unittest
from lost_hat_login_tests import LostHatLoginTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatLoginTests('test_logging_positive'))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())
