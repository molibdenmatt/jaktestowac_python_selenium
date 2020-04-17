import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from helpers import operational_helpers as oh


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'

    @classmethod
    def tearDown(self):
        self.driver.quit()

    # helper functions
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

    # Smoke page title tests:
    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    def test_product_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_product_url, expected_title)

    def test_product_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_product_url, expected_title)

    def test_product_art_page_title(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    def test_login_page_title(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)

    def test_search_bar(self):
        driver = self.driver
        driver.get(self.base_url)
        search_results_header = '//*[text()="Search results"]'
        search_result_miniature = '//article[contains(@class, "product-miniature")]'
        # Search mug product
        search_input = driver.find_element_by_xpath('//input[@placeholder="Search our catalog"]')
        search_input.send_keys('mug')
        search_input.send_keys(Keys.ENTER)
        # wait for search results page
        oh.visibility_of_element_wait(driver, search_results_header)
        list_of_search_results = oh.visibility_of_all_elements_wait(driver, search_result_miniature)
        # Assert at least one product is visible in results
        self.assertGreaterEqual(len(list_of_search_results), 1)


