import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helpers import functional_helpers


class LostHatLoginTests(unittest.TestCase):
    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = 'https://autodemo.testoneo.com/en/'
        self.login_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differs from actual on page: {driver.current_url}')

    def test_login_page(self):
        driver = self.driver
        driver.get(self.login_page)
        expected_header = 'Log in to your account'
        self.assert_element_text(driver, '//header[@class="page-header"]/h1', expected_header )

    def test_logging_positive(self):
        user_email = 'sux.effect@gmail.com'
        user_pass = '*V43g%Ss7EEx'

        driver = self.driver
        driver.get(self.login_page)

        functional_helpers.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, '//header[@class="page-header"]//h1', 'Your account')

    def test_logging_negative(self):
        user_email = 'abc@def.gh'
        user_pass = 'testpass'

        driver = self.driver
        driver.get(self.login_page)

        functional_helpers.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, '//*[@class = "alert alert-danger"]', 'Authentication failed.')





