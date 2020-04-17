import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_elements(driver, xpath, time_to_wait=5, number_of_expected_elements=1):
    """
    Checking every second if list of elements under specified xpath was found
    :param number_of_expected_elements: min. number elements are to be found (default: 1)
    :param driver: webdriver instance
    :param xpath: element to look for
    :param time_to_wait: max time to wait (default: 5)
    :return list of found elements
    """
    for seconds in range(time_to_wait):
        elements = driver.find_elements_by_xpath(xpath)
        number_of_elements = len(elements)
        if number_of_elements >= number_of_expected_elements:
            return elements
        if seconds == time_to_wait - 1:
            assert len(elements) >= number_of_expected_elements, f'Expected {number_of_expected_elements} ' \
                                                                 f'elements but found {len(elements)} for xpath ' \
                                                                 f'{xpath} in time of {time_to_wait}s'
        time.sleep(1)


def visibility_of_element_wait(driver, element_xpath, timeout=10):
    """
    Checking if specified by xpath element is visible on the page
    Using selenium wait
    :param timeout: Max time to wait (default: 10)
    :param driver: Webdriver object
    :param element_xpath: Xpath for the element to be visible
    :return: found element or error_message
    """
    error_message = f'Element {element_xpath} not found on {driver.current_url}'
    locator = (By.XPATH, element_xpath)
    element_located = ec.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout)

    return wait.until(element_located, error_message)

