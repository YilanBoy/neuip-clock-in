import configparser
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver

from get_element import *

# 取得設定檔的參數
current_directory_path = os.path.dirname(__file__)
config_file_path = os.path.join(current_directory_path, 'config.ini')
config = configparser.RawConfigParser()
config.read(config_file_path)

# 取得上班時間
clock_in_time = datetime.now().replace(
    hour=int(config['CLOCK_IN']['hour']),
    minute=int(config['CLOCK_IN']['minute']))

# 取得下班時間
clock_out_time = datetime.now().replace(
    hour=int(config['CLOCK_OUT']['hour']),
    minute=int(config['CLOCK_OUT']['minute']))


# 登入
def login(browser: WebDriver):
    browser.get(config['WEBSITE']['login_url'])

    browser.implicitly_wait(10)

    get_element_by_id(browser, 'username_input').send_keys(
        config['WEBSITE']['username'])

    get_element_by_id(browser, 'password-input').send_keys(
        config['WEBSITE']['password'])

    get_element_by_id(browser, 'login-button').click()


# 點擊打上班卡的按鈕
def click_the_clock_in_button(browser: WebDriver):
    element = get_element_by_selector(browser, config['CLOCK_IN']['selector'])

    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.click()
    actions.perform()


# 點擊打下班卡的按鈕
def click_the_clock_out_button(browser: WebDriver):
    element = get_element_by_selector(browser, config['CLOCK_OUT']['selector'])

    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.click()
    actions.perform()


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


# 根據時間打上下班的卡
def clock_in_or_clock_out(browser: WebDriver):
    browser.get(config['WEBSITE']['target_url'])

    browser.implicitly_wait(10)

    if datetime.now() < clock_in_time:
        clock_in(browser)

    if datetime.now() > clock_out_time:
        clock_out(browser)

    if datetime.now() > clock_in_time and datetime.now() < clock_out_time:
        if is_clock_in(browser):
            print('already clocked in')
        else:
            print('you were late!')
            clock_in(browser)


# 檢查是否已經打上班卡
def is_clock_in(browser: WebDriver) -> bool:

    retry = 0
    while "clock_btn2" not in get_element_by_selector(browser, config['CLOCK_IN']['selector']).get_attribute('class'):

        retry += 1
        if retry > 3:
            return False

        time.sleep(3)

    return True


# 檢查是否已經打下班卡
def is_clock_out(browser: WebDriver) -> bool:

    retry = 0
    while "clock_btn2" not in get_element_by_selector(browser, config['CLOCK_OUT']['selector']).get_attribute('class'):

        retry += 1
        if retry > 3:
            return False

        time.sleep(3)

    return True


def main():
    options = Options()
    service = Service(log_path=os.path.devnull)
    options.headless = True

    # 偽造公司的地理坐標
    options.set_preference(
        'geo.wifi.uri', 'data:application/json,{"location": {"lat": 25.04561, "lng":121.54891}, "accuracy": 20.0}')
    options.set_preference("geo.prompt.testing", True)

    browser = webdriver.Firefox(
        options=options, service=service)

    login(browser)
    clock_in_or_clock_out(browser)

    browser.close()


if __name__ == '__main__':
    main()
