from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
driver.get(url)
title = driver.title
print(f'Actual title: {title}')
login_form_header_elements = driver.find_elements_by_xpath('//*[@id="login_form"]/h1')
print(f'Actual number of h1 elements: {len(login_form_header_elements)}')

login_form_header_element = login_form_header_elements[0]
login_form_header_text = login_form_header_element.text
print(f'Login form header text: {login_form_header_text}')

login_input_element = driver.find_element_by_xpath('//*[@id="login_id"]')
# .text returns hardcoded value from DOM. To get value from the user input we have to use get_attribute method

print(f'Input box text before send_keys(): {login_input_element.get_attribute("value")}')
login_input_element.send_keys('kocur13d')
print(f'Input box text after send_keys(): {login_input_element.get_attribute("value")}')
time.sleep(1)
login_input_element.send_keys(Keys.BACKSPACE)
time.sleep(1)
login_input_element.clear()
print(f'Input box text after clear(): {login_input_element.get_attribute("value")}')
time.sleep(1)

dalej_button = driver.find_element_by_id('login_next')
# get string value of disabled
dalej_button_disabled = dalej_button.get_attribute("disabled")
if dalej_button_disabled == "true":
    print(dalej_button_disabled)

# get bool value of disabled
dalej_button_disabled_bool = dalej_button.get_property('disabled')
if dalej_button_disabled_bool == True:
    print(dalej_button_disabled_bool)

login_reminder_element = driver.find_element_by_id('ident_rem')
login_reminder_element.click()
time.sleep(1)
login_reminder_close_button = driver.find_element_by_class_name('shadowbox-close')
login_reminder_close_button.click()

login_input_element.send_keys('asdftrsvbbb', Keys.ENTER)
saved_login_value = login_input_element.get_attribute("value")
print(f'Typed vaule: asdftrsvbbb, Saved value: {saved_login_value}')
driver.quit()