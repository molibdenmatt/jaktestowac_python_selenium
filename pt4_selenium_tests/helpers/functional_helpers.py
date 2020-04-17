import time


def user_login(driver, user_email, user_pass):
    """
    Allows to enter login & password to inputs and click 'Submit' button

    :param driver: webdriver instance
    :param user_email: user e-mail
    :param user_pass: user password
    :returns none
    """
    # Enter e-mail
    login_input = driver.find_element_by_xpath('//*[@name="email" and @class="form-control"]')
    login_input.send_keys(user_email)
    # Enter password
    password_input = driver.find_element_by_xpath('//*[@name="password"]')
    password_input.send_keys(user_pass)
    # Click login button
    driver.find_element_by_id('submit-login').click()
    time.sleep(2)

