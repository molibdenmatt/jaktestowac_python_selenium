import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helpers import functional_helpers


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