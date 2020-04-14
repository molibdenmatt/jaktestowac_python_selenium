import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helpers import functional_helpers


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = 'https://autodemo.testoneo.com/en/'
        self.login_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        self.clothes_page = 'https://autodemo.testoneo.com/en/3-clothes'
        self.accessories_page = 'https://autodemo.testoneo.com/en/6-accessories'
        self.art_page = 'https://autodemo.testoneo.com/en/9-art'

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def assert_correct_title(self, url, expected_title):
        driver = self.driver
        driver.get(url)
        title = driver.title
        self.assertEqual(expected_title, title,
                         f'Expected title differs from actual for page url: {url}')

    def test_titles(self):
        with self.subTest():
            self.assert_correct_title(self.main_page, 'Lost Hat')
            self.assert_correct_title(self.login_page, 'Login')
            self.assert_correct_title(self.art_page, 'Art')
            self.assert_correct_title(self.clothes_page, 'Clothes')
            self.assert_correct_title(self.accessories_page, 'Accessories')

