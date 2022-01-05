import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver

from src.config import get_config
from src.get_element import *

# 取得設定檔的參數
config = get_config()


# 進行打下班卡作業
def clock_out(browser: WebDriver):

    if is_clock_out(browser):
        print('time to clock out, but you already clocked out')
    else:
        print('time to clock out')

        click_the_clock_out_button(browser)

        if is_clock_out(browser):
            print('clock out success')
        else:
            print('clock out failed')


# 檢查是否已經打下班卡
def is_clock_out(browser: WebDriver) -> bool:

    retry = 0
    while "clock_btn2" not in get_element_by_selector(browser, config['CLOCK_OUT']['selector']).get_attribute('class'):

        retry += 1
        if retry > 3:
            return False

        time.sleep(3)

    return True


# 點擊打下班卡的按鈕
def click_the_clock_out_button(browser: WebDriver):
    element = get_element_by_selector(browser, config['CLOCK_OUT']['selector'])

    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.click()
    actions.perform()