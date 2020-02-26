import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):  # Runs before each test
        pass

    def tearDown(self):
        pass

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(f'Actual title of visited page: {title}')
        assert title == 'Demobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        title = 20
        print(f'Actual title: {title}')

    def test_main_page(self):
        driver = self.driver
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title
