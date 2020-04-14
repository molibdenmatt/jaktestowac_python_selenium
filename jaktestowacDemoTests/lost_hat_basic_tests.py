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


class LostHatFrontPageTests(unittest.TestCase):

    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = 'https://autodemo.testoneo.com/en/'
        self.login_page = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_main_slider_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'

        driver = self.driver
        driver.get(self.main_page)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        self.assertLess(expected_min_height, actual_slider_height)
        self.assertLess(expected_min_width, actual_slider_width)

    def test_slider_elements_number(self):
        expected_number_of_slides = 3
        slider_xpath = '//ul[@class="carousel-inner"]/li'

        driver = self.driver
        driver.get(self.main_page)

        slider_elements = driver.find_elements_by_xpath(slider_xpath)
        self.assertEqual(expected_number_of_slides, len(slider_elements),
                         f'Number of slider element differs from expected')

    def test_slider_elements_titles(self):
        slide_title_xpath = '//ul[@class="carousel-inner"]/li//*[contains(@class, "text-uppercase")]'
        driver = self.driver
        driver.get(self.main_page)
        """
        with self.subTest method allows to run many assertions without stopping on failed one
        """
        slides_list = driver.find_elements_by_xpath(slide_title_xpath)
        for slide in slides_list:
            slide_title = slide.get_attribute('textContent').lower()
            with self.subTest(slide_title):
                self.assertTrue('sample' in slide_title, f'Actual slide title differs on {self.main_page}')

    def test_promo_elements(self):
        expected_number_of_items = 8
        driver = self.driver
        driver.get(self.main_page)
        class_name = "product-miniature.js-product-miniature"
        items_list = driver.find_elements_by_class_name(class_name)
        self.assertEqual(expected_number_of_items, len(items_list))

