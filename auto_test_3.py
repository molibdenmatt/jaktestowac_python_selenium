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
