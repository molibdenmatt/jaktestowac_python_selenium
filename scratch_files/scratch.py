import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"/chromedriver")

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()