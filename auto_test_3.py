import unittest
import time
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

    def test_login_lenght_message(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        identity_input = driver.find_element_by_id('login_id')
        identity_input.clear()
        identity_input.send_keys("asbsdrt")
        login_tooltip_button = driver.find_elements_by_class_name('login-tooltip')[0]
        login_tooltip_button.click()
        login_error_message = driver.find_element_by_class_name('error').text
        self.assertEqual('identyfikator ma min. 8 znaków', login_error_message,
                         f'Message differs from expected one. Found:{login_error_message}')

    def test_correct_login_input(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        # Login input - enter login
        identity_input = driver.find_element_by_id('login_id')
        identity_input.clear()
        identity_input.send_keys("asdfgklo")
        driver.find_element_by_id('login_next').click()
        time.sleep(2)
        # Check if "Zaloguj sie" button is visible
        login_next_button_content = driver.find_element_by_id('login_next').text
        self.assertEqual('zaloguj się', login_next_button_content)

    def test_login_reminder(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(url)
        remind_login_button = driver.find_element_by_id('ident_rem')
        remind_login_button.click()
        time.sleep(1)
        remind_login_popup_text = driver.find_element_by_xpath('//div[contains(@class, "contact-popup")]//h2').text
        self.assertEqual('ta funkcja jest niedostępna', remind_login_popup_text,
                         f'Incorrect popup message for login reminder')

    def test_correct_credentials(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/logowanie_etap_2.html"
        driver.get(url)
        # Enter login and Password
        identity_input = driver.find_element_by_id('login_id')
        identity_input.send_keys("asdfgklo")
        password_input = driver.find_element_by_id('login_password')
        password_input.send_keys("password1")
        login_next_button = driver.find_element_by_id('login_next')
        login_next_button.click()
        time.sleep(2)
        # Check if login was successful
        logout_button = driver.find_element_by_xpath('//a[contains(@class, "btn logout")]')
        self.assertEqual('Wyloguj', logout_button.text, f'Logging in to the system not successful')
        time.sleep(3)


