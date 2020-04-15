from selenium import webdriver

driver = webdriver.Chrome(executable_path='../chromedriver')
driver.get('https://www.discuvver.com/')

driver.find_element_by_xpath("//button[contains(text(), 'Take me to a useful website')]").click()

title = driver.title
print(title)

# assert title == 'Demobank - Bankowość Internetowa - Logowanie'

driver.quit()
