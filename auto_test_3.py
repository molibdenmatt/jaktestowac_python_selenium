import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_demo_login(self):
        driver = self.driver
        site = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(site)
        title = driver.title
        print(f'Actual title: {title}')
        # assert 'Demobank - Bankowość Internetowa - Logowanie' == title
        self.assertEqual(f'Demobank - Bankowość Internetowa - Logowanie', title,
                         msg='Expected title differ from actual for page url: '
                             f'{site}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
