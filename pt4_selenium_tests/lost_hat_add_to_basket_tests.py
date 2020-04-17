import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helpers import operational_helpers as oh


class LostHatBasketTests(unittest.TestCase):
    @classmethod
    def setUp(self):  # Runs before each test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = 'https://autodemo.testoneo.com/en/'
        self.art_page = 'https://autodemo.testoneo.com/en/9-art'

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

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.art_page)
        fox_vector_product = driver.find_element_by_xpath('//*[text() = "Mountain fox - Vector graphics"]')
        fox_vector_product.click()

        add_to_cart_button_xpath = '//button[@data-button-action="add-to-cart"]'
        add_to_cart_button = oh.visibility_of_element_wait(driver, add_to_cart_button_xpath)
        add_to_cart_button.click()

        modal_success_xpath = '//*[@id="myModalLabel"]'
        expected_success_alert = 'Product successfully added to your shopping cart'

        # Using custom wait method:
        # confirmation_modal_elements = oh.wait_for_elements(driver, modal_success_xpath, 5)
        # success_text = confirmation_modal_elements[0].text

        confirmation_modal_elements = oh.visibility_of_element_wait(driver, modal_success_xpath)
        self.assertEqual(expected_success_alert, confirmation_modal_elements.text)



