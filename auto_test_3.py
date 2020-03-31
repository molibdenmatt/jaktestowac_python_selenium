import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_demo_login(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        # assert 'Demobank - Bankowość Internetowa - Logowanie' == title
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Expected title differ from actual for page url: {url}')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_title(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        page_h1_title = driver.find_element_by_xpath("//div[contains(@class, 'login-container')]//h1").text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', page_h1_title,
                         f'Expected title differ from actual title for page url: {url}')

    def test_is_login_disabled(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        identity_input = driver.find_element_by_id('login_id')
        identity_input.clear()
        login_next_button = driver.find_element_by_id('login_next')
        login_next_button_disabled = login_next_button.get_property('disabled')
        self.assertEqual(True, login_next_button_disabled,
                         f'Expected state of "dalej" button: True , differ from actual: '
                         f'{login_next_button_disabled} , for page url: {url}')
