from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/mateuszswieton/private_stuff/jaktestowac_python_selenium/chromedriver')
# driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
driver.get('https://www.discuvver.com/')

driver.find_element_by_xpath("//button[contains(text(), 'Take me to a useful website')]").click()

title = driver.title
print(title)

assert title == 'Demobank - Bankowość Internetowa - Logowanie'

driver.quit()
