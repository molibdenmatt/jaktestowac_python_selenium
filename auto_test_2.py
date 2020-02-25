import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/mateuszswieton/private_stuff/jaktestowac_python_selenium/chromedriver')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):  # Runs before each test
        pass

    def tearDown(self):
        pass

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Konta'

    def test_main_page(self):
        driver = self.driver
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title
