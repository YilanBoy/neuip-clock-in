import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver

from src.clock_in import *
from src.clock_out import *
from src.config import get_config
from src.get_element import *

# 取得設定檔的參數
config = get_config()

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


# 根據時間打上下班的卡
def clock_in_or_clock_out(browser: WebDriver):
    browser.get(config['WEBSITE']['target_url'])

    browser.implicitly_wait(10)

    if datetime.now() < clock_in_time:
        if not is_clock_in(browser):
            clock_in(browser)

        return

    if datetime.now() > clock_in_time and datetime.now() < clock_out_time:
        if not is_clock_in(browser):
            clock_in(browser)

        return

    if datetime.now() > clock_out_time:
        if not is_clock_out(browser):
            clock_out(browser)

        return


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
