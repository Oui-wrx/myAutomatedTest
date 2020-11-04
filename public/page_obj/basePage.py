# -*- coding: utf-8 -*-
# @Author  : wrx
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self,  driver: WebDriver = None):
        if driver is None:
            # 浏览器复用
            # options = Options()
            # options.debugger_address = "127.0.0.1:5678"
            # self._driver = webdriver.Chrome(options=options)
            self._driver = webdriver.Chrome()
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
        # print(loc)
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

    def set_calendar(self, year, month, day):
        """
        时间段设置
        :return:
        """
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


# class BasePage:
#     """
#     基础页面类，用于其他页的继承
#     """
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_ok(self):
#         """
#         适用于仅有确定的弹框
#         """
#         self.driver.find_element(By.CSS_SELECTOR, "div.el-message-box__btns > button").click()
#

#
#     def open(self):
#         """
#         打开登录入口
#         """
#         self.driver.get(url)
#


#
#     def execute_script_click(self, element):
#         """
#         使用js执行点击
#         """
#         try:
#             self.driver.execute_script("arguments[0].click();", element)
#         except JavascriptException:
#             element.click()
#
#     def switch_frame(self, loc):
#         """
#         多表单嵌套切换
#         :param loc: 传元素的属性值
#         :return: 定位到的元素
#         """
#         return self.driver.switch_to.frame(loc)
#         # 关于异常处理
#
#     def switch_windows(self, loc):
#         """
#         多窗口切换
#         :param loc:
#         :return:
#         """
#         return self.driver.switch_to_window(loc)
#         # 关于异常处理
#
#     def switch_alert(self):
#         """
#         弹框处理
#         :return:
#         """
#         return self.driver.switch_to.alert.accept()
#         # 关于异常处理
#
#     def switch_to_alert(self):
#         """
#         进入alert
#         :return:
#         """
#         return self.driver.switchTo().alert()
#
#     def click_nok_close(self):
#         """
#         点击取消，关闭弹框
#         :return:
#         """
#         self.driver.find_element(By.XPATH, "//button/span[contains(text(), '取消')]").click()
#
#     def find_elements_by_text(self, text):
#         """
#         根据关键字定位元素
#         待测试
#         :param text:
#         :return:
#         """
#         s = "[contains(text(), '" + text + "')]"
#         if self.find_elements(By.XPATH, "//p" + s):
#             return self.find_elements(By.XPATH, "//p" + s)
#         elif self.find_elements(By.XPATH, "//li/div" + s):
#             return self.find_elements(By.XPATH, "//li/div" + s)
#         elif self.find_elements(By.XPATH, "//button/span" + s):
#             return self.find_elements(By.XPATH, "//button/span" + s)
#         elif self.find_elements(By.XPATH, "//li" + s):
#             return self.find_elements(By.XPATH, "//li" + s)
#         elif self.find_elements(By.XPATH, "//span" + s):
#             return self.find_elements(By.XPATH, "//span" + s)
#         elif self.find_elements(By.XPATH, "//div" + s):
#             return self.find_elements(By.XPATH, "//div" + s)
#         else:
#             return 0
#
#     def find_element_by_link_text(self, text_value):
#         """
#         link_text查找元素
#         :param text_value:
#         :return:
#         """
#         return self.driver.find_element_by_link_text(text_value)
#

#
#     def open_message(self):
#         """
#         打开消息
#         :return:
#         """
#
#     def get_element_innerText(self, element):
#         """
#         获取标签内的文本
#         :param element:
#         :return:
#         """
#         return element.get_attribute('innerText')


if __name__ == '__main__':
    # base = BasePage()
    pass
