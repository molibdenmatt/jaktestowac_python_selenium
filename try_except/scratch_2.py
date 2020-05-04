from selenium import webdriver
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://antoogle.testoneo.com/')

xpath_list = ['*yolo_this_is_not_xpath*', '//*[@class="this xpath cannot be found"]', '//*[@class="h6 mb-3 font-weight-normal"]']

for xpath in xpath_list:
    try:
        elem = driver.find_element_by_xpath(xpath)
    except InvalidSelectorException as syntax_error:
        print(f'XPath {xpath} is broken!')
        print(syntax_error)
    except NoSuchElementException as no_elem_error:
        print(f"Element with '{xpath}' not found")
        print(no_elem_error)
    else:
        print(elem.text)

driver.quit()