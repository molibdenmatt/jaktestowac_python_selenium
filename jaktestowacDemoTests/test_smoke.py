import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = 'https://autodemo.testoneo.com/en/'
        self.login_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        self.login = 'sux.effect@gmail.com'
        self.pswd = '*V43g%Ss7EEx'

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login_page(self):
        driver = self.driver
        driver.get(self.login_page)
        expected_header = 'Log in to your account'

        login_page_header = driver.find_element_by_xpath('//header[@class="page-header"]/h1')
        self.assertEqual(expected_header, login_page_header.text,
                         f'Login header differs from expected for {self.login_page}')

    def test_logging_in(self):
        driver = self.driver
        driver.get(self.login_page)

        login_input = driver.find_element_by_xpath('//*[@name="email" and @class="form-control"]')
        login_input.send_keys(self.login)
        password_input = driver.find_element_by_xpath('//*[@name="password"]')
        password_input.send_keys(self.pswd)

        driver.find_element_by_id('submit-login').click()
        time.sleep(2)

        logged_account_header = driver.find_element_by_xpath('//header[@class="page-header"]//h1').text
        self.assertEqual('Your account', logged_account_header, f'Not logged in correctly')

    def test_tshirt_name_and_price(self):
        driver = self.driver
        driver.get(self.product_page)
        expected_price = '23.52'
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'

        product_name = driver.find_element_by_xpath('//*[@itemprop="name" and @class="h1"]').text
        self.assertEqual(expected_name, product_name, f'Product name not as expected. Found:{product_name}')

        product_price = driver.find_element_by_xpath('//*[@itemprop = "price"]').text[3:]
        self.assertEqual(expected_price, product_price, f'Price mismatch. Found:{product_price}')
