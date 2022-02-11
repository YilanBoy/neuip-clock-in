import time
from datetime import datetime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver

from src.config import get_config
from src.get_element import *
from src.jandi import send_message

# 取得設定檔的參數
config = get_config()


# 進行打上班卡作業
def clock_in(browser: WebDriver):
    current_datetime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    click_the_clock_in_button(browser)

    if is_clock_in(browser):
        message = f'🗓 {current_datetime}\n💼 clock in\n✅ success'
        print(message)
        send_message(message)
    else:
        message = f'🗓 {current_datetime}\n💼 clock in\n❌ failed'
        print(message)
        send_message(message)


# 檢查是否已經打上班卡
def is_clock_in(browser: WebDriver) -> bool:

    retry = 0
    # 必須使用雙引號，否則即使 class name 存在也會回傳 False
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
