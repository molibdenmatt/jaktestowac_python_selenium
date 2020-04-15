import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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




