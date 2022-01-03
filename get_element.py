import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


# 使用 selector 取得元素
def get_element_by_selector(browser: WebDriver, selector: str):
    try:
        element = browser.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        browser.close()
        sys.exit('No element')

    return element


# 使用完整 xpath 取得元素
def get_element_by_xpath(browser: WebDriver, xpath: str):
    try:
        element = browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        browser.close()
        sys.exit('No element')

    return element


# 使用 id 取得元素
def get_element_by_id(browser: WebDriver, id: str):
    try:
        element = browser.find_element(By.ID, id)
    except NoSuchElementException:
        browser.close()
        sys.exit('No element')

    return element
