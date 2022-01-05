import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver

from src.config import get_config
from src.get_element import *

# 取得設定檔的參數
config = get_config()


# 進行打上班卡作業
def clock_in(browser: WebDriver):

    if is_clock_in(browser):
        print('time to clock in, but you have already clocked in')
    else:
        print('time to clock in')

        click_the_clock_in_button(browser)

        if is_clock_in(browser):
            print('clock in success')
        else:
            print('clock in failed')


# 檢查是否已經打上班卡
def is_clock_in(browser: WebDriver) -> bool:

    retry = 0
    while "clock_btn2" not in get_element_by_selector(browser, config['CLOCK_IN']['selector']).get_attribute('class'):

        retry += 1
        if retry > 3:
            return False

        time.sleep(3)

    return True


# 點擊打上班卡的按鈕
def click_the_clock_in_button(browser: WebDriver):
    element = get_element_by_selector(browser, config['CLOCK_IN']['selector'])

    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.click()
    actions.perform()
