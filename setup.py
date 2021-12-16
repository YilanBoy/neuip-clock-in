import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.webdriver import WebDriver
from datetime import datetime

# 取得設定檔的參數
config = configparser.RawConfigParser()
config.read('config.ini')


def login(browser: WebDriver):
    browser.get(config['WEBSITE']['login_url'])

    # 輸入帳號密碼並登入
    browser.find_element(By.ID, 'dept_input').send_keys(
        config['WEBSITE']['company_code'])
    browser.find_element(By.ID, 'username_input').send_keys(
        config['WEBSITE']['employee_code'])
    browser.find_element(By.ID, 'password-input').send_keys(
        config['WEBSITE']['password'])

    browser.find_element(By.ID, "login-button").click()


# 根據時間打上下班的卡
def punch_in_or_punch_out(browser: WebDriver):

    browser.get(config['WEBSITE']['target_url'])

    clock_in_time = datetime.now().replace(
        hour=int(config['CLOCK_IN']['hour']),
        minute=int(config['CLOCK_IN']['minute']))

    clock_out_time = datetime.now().replace(
        hour=int(config['CLOCK_OUT']['hour']),
        minute=int(config['CLOCK_OUT']['minute']))

    if (datetime.now() < clock_in_time):
        browser.find_element(
            By.XPATH, config['CLOCK_IN']['xpath']).click()

    if (datetime.now() > clock_out_time):
        browser.find_element(
            By.XPATH, config['CLOCK_OUT']['xpath']).click()


def main():
    options = Options()
    firefox_profile = FirefoxProfile()
    # 偽造公司的地理坐標
    firefox_profile.set_preference(
        'geo.wifi.uri', 'data:application/json,{"location": {"lat": 25.04561, "lng":121.54891}, "accuracy": 20.0}')
    firefox_profile.set_preference("geo.prompt.testing", True)
    options.profile = firefox_profile
    browser = webdriver.Firefox(options=options)

    login(browser)
    punch_in_or_punch_out(browser)

    time.sleep(10)

    browser.close()


if __name__ == '__main__':
    main()
