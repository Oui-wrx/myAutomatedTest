# -*- coding: utf-8 -*-
# @Author  : wrx

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config.setting import SCREENSHOOT


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self,  driver: WebDriver = None):
        if driver is None:
            # 浏览器复用  能力有限  目前的测试环境 自己尝试未果
            # 个人资料路径
            # user_data_dir = r'--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data'
            # options = Options()
            # options.debugger_address = "127.0.0.1:9222"
            # options.add_argument(user_data_dir)
            # self._driver = webdriver.Chrome(options=options)
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', False)
            self._driver = webdriver.Chrome(options=options)
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, eleName):
        """
        根据定位器  查找单个元素
        """
        loc = (eleName["by"], eleName["locator"])
        print(loc)
        try:
            WebDriverWait(self._driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self._driver.find_element(*loc)
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def finds(self, eleName):
        """
        根据定位器  查找多个元素
        """
        loc = (eleName["by"], eleName["locator"])
        try:
            WebDriverWait(self._driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self._driver.find_elements(*loc)
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def wait_for(self, eleName):
        """
        等待元素可被点击
        """
        loc = (eleName["by"], eleName["locator"])
        WebDriverWait(self._driver, 10, 0.5).until(EC.element_to_be_clickable(loc))

    def get_page_source(self):
        """
        获取html源码
        """
        return self._driver.page_source

    def get_driver(self):
        """
        返回驱动
        """
        return self._driver

    def set_driver(self, driver):
        self._driver = driver

    def click_cancell(self):
        """
        用于弹框中出现取消的情况
        """
        self._driver.find_element(By.CSS_SELECTOR, "div.w-message-box__btns > button").click()

    def click_confirm(self):
        """
        用于弹框出现确定的情况
        """
        # sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, "div.w-message-box__btns > button + button").click()

    def on_page(self, Url):
        """
        判断当前页与预期一致
        """
        return self._driver.current_url == Url

    def back(self):
        """
        页面回退
        """
        self._driver.back()

    def execute_script(self, js):
        """
        执行js脚本
        """
        self._driver.execute_script(js)

    def scroll_page_by_js(self, direction):
        """
        页面滑动
        """
        if direction == "up":
            self.execute_script("document.documentElement.scrollTop=0")
        elif direction == "down":
            self.execute_script("document.documentElement.scrollTop=1000")
        elif direction == "left":
            self.execute_script("document.documentElement.scrollLeft=0")
        else:
            self.execute_script("document.documentElement.scrollLeft=1000")

    def set_calendar(self, year, month, day):
        """
        时间段设置   这样费劲  是因为  采用js的设置没成功  有时间研究一下
        :return:
        """
        year = int(year)
        month = int(month)
        day = int(day)
        # 获取年月标签元素
        element = self._driver.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
        # 获取标签的年
        now_year = element.get_attribute('innerText')[0:4]
        # 寻找目标的年月
        while year > int(now_year):
            self._driver.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-d-arrow-right']").click()
            # 获取年月标签元素
            element = self._driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/div/div")
            # 获取标签的年
            now_year = element.get_attribute('innerText')[0:4]
        while year < int(now_year):
            self._driver.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-d-arrow-left']").click()
            # 获取年月标签元素
            element = self._driver.find_element(By.CLASS_NAME, "el-icon-d-arrow-left")
            # 获取标签的年
            now_year = element.get_attribute('innerText')[0:4]
        # 获取年月标签元素
        element = self._driver.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
        # 获取标签的月
        if element.get_attribute('innerText')[8:9] == " ":
            now_month = element.get_attribute('innerText')[7:8]
        else:
            now_month = element.get_attribute('innerText')[7:9]
        # 寻找目标的月
        while month > int(now_month):
            self._driver.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-arrow-right']").click()
            # 获取年月标签元素
            element = element = self._driver.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
            # 获取标签的月
            if element.get_attribute('innerText')[8:9] == " ":
                now_month = element.get_attribute('innerText')[7:8]
            else:
                now_month = element.get_attribute('innerText')[7:9]
        while month < int(now_month):
            self._driver.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-arrow-left']").click()
            # 获取年月标签元素
            element = self._driver.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
            # 获取标签的月
            if element.get_attribute('innerText')[8:9] == " ":
                now_month = element.get_attribute('innerText')[7:8]
            else:
                now_month = element.get_attribute('innerText')[7:9]
        # 点击目标的日
        self._driver.find_element(By.XPATH, "//tr/td/div/span[contains(text(), '20')]").click()

    def take_screenshot(self, screen_name):
        file_path = SCREENSHOOT
        try:
            screen_name = file_path + screen_name
            # self._driver.get_screenshot_as_file(screen_name)
            self._driver.save_screenshot(screen_name)
        except Exception as e:
            return False


if __name__ == '__main__':
    # base = BasePage()
    pass
