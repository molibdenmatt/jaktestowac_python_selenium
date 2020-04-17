import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from helpers import operational_helpers as oh


class LostHatProductTests(unittest.TestCase):
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
        """Comparing expected text with observed value from web element
                :param driver: webdriver instance
                :param xpath: xpath to element with text to be observed
                :param expected_text: text what we expect to be found
                :return: None
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differs from actual on page: {driver.current_url}')

    def test_tshirt_name(self):
        driver = self.driver
        driver.get(self.product_page)
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(driver, '//*[@itemprop="name" and @class="h1"]', expected_name)

    def test_tshirt_price(self):
        driver = self.driver
        driver.get(self.product_page)
        expected_price = 'PLN23.52'
        self.assert_element_text(driver, '//*[@itemprop = "price"]', expected_price)

    def test_search_results(self):
        driver = self.driver
        driver.get(self.product_page)
        expected_no_of_results = 2
        search_results_header = '//*[text()="Search results"]'
        search_result_product = '//h1[contains(@class, "product-title")]//a'

        # Search printed product
        search_input = driver.find_element_by_xpath('//input[@placeholder="Search our catalog"]')
        search_input.send_keys('printed')
        search_input.send_keys(Keys.ENTER)

        # wait for search results page
        oh.visibility_of_element_wait(driver, search_results_header)
        list_of_search_results = oh.visibility_of_all_elements_wait(driver, search_result_product)
        found_matching_products = 0
        for product in list_of_search_results:
            if 'printed' in product.text.lower():
                found_matching_products += 1
        # Assert at least one product is visible in results
        self.assertEqual(found_matching_products, expected_no_of_results)





