# -*- coding: utf-8 -*-
# @Author  : wrx
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "http://172.16.0.166:8034/index.html"


class BasePage:
    """
    基础页面类，用于其他页的继承
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """
        内部调用_open私有函数
        :return:
        """
        self.driver.get(url)
        # self.driver.implicity_wait(10)

    def on_page(self):
        """
        url地址断言
        :return:url地址
        """
        # return self.driver.current_url == (self.base_url + self.url)
        pass

    def find_element(self, *loc):
        """
        单个元素定位
        :param loc:
        :return:
        """
        try:
            # 显示等待  10：超时的总时长 0.5：循环去查询的间隙时间，默认0.5秒
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            # driver.implicity_wait(10) 实际上浏览器会在你自己设定的时间内部断的刷新页面去寻找我们需要的元素
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            return False

    def find_elements(self, *loc):
        """
        多个元素定位
        :param loc: 传入元素的属性
        :return: 定位到的元素
        """
        print(*loc)
        try:
            return self.driver.find_elements(*loc)
        except:
            print("元素没找到")
            return False

    def script(self, src):
        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: javaScript脚本
        """
        return self.driver.execute_script(src)

    def send_key(self, *loc, value):
        """
        重定义send_keys方法
        :param loc:
        :param value:
        :return:
        """
        # self.find_element(*loc).click()
        self.find_element(*loc).clear().send_keys(value)
        # self.find_element(*loc)

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        return self.driver.switch_to.frame(loc)
        # 关于异常处理

    def switch_windows(self, loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        return self.driver.switch_to_window(loc)
        # 关于异常处理

    def switch_alert(self):
        """
        弹框处理
        :return:
        """
        return self.driver.switch_to.alert.accept()
        # 关于异常处理

    def switch_to_alert(self):
        """
        进入alert
        :return:
        """
        return self.driver.switchTo().alert()

    def click_ok_close(self):
        """
        点击确定，关闭弹框
        :return:
        """
        self.driver.find_element(By.XPATH, "//button/span[contains(text(), '确定')]").click()

    def click_nok_close(self):
        """
        点击取消，关闭弹框
        :return:
        """
        self.driver.find_element(By.XPATH, "//button/span[contains(text(), '取消')]").click()

    def find_element_by_text(self, text):
        """
        根据关键字定位元素
        待测试
        :param text:
        :return:
        """
        s = "[contains(text(), '" + text + "')]"
        if self.find_element(By.XPATH, "//div/p" + s):
            return self.find_element(By.XPATH, "//div/p" + s)
        elif self.find_element(By.XPATH, "//li/div" + s):
            return self.find_element(By.XPATH, "//li/div" + s)
        elif self.find_element(By.XPATH, "//button/span" + s):
            return self.find_element(By.XPATH, "//button/span" + s)
        elif self.find_element(By.XPATH, "//li" + s):
            return self.find_element(By.XPATH, "//li" + s)
        elif self.find_element(By.XPATH, "//span" + s):
            return self.find_element(By.XPATH, "//span" + s)
        elif self.find_element(By.XPATH, "//div" + s):
            return self.find_element(By.XPATH, "//div" + s)
        elif self.find_element(By.XPATH, "//button" + s):
            return self.find_element(By.XPATH, "//button" + s)
        else:
            return 0

    def find_elements_by_text(self, text):
        """
        根据关键字定位元素
        待测试
        :param text:
        :return:
        """
        s = "[contains(text(), '" + text + "')]"
        if self.find_elements(By.XPATH, "//p" + s):
            return self.find_elements(By.XPATH, "//p" + s)
        elif self.find_elements(By.XPATH, "//li/div" + s):
            return self.find_elements(By.XPATH, "//li/div" + s)
        elif self.find_elements(By.XPATH, "//button/span" + s):
            return self.find_elements(By.XPATH, "//button/span" + s)
        elif self.find_elements(By.XPATH, "//li" + s):
            return self.find_elements(By.XPATH, "//li" + s)
        elif self.find_elements(By.XPATH, "//span" + s):
            return self.find_elements(By.XPATH, "//span" + s)
        elif self.find_elements(By.XPATH, "//div" + s):
            return self.find_elements(By.XPATH, "//div" + s)
        else:
            return 0

    def find_element_by_link_text(self, text_value):
        """
        link_text查找元素
        :param text_value:
        :return:
        """
        return self.driver.find_element_by_link_text(text_value)

    def set_calendar(self, year, month, day):
        """
        时间段设置
        :return:
        """
        # 获取年月标签元素
        element = self.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
        # 获取标签的年
        now_year = element.get_attribute('innerText')[0:4]
        # 寻找目标的年月
        while year > int(now_year):
            self.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-d-arrow-right']").click()
            # 获取年月标签元素
            element = self.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/div/div")
            # 获取标签的年
            now_year = element.get_attribute('innerText')[0:4]
        while year < int(now_year):
            self.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-d-arrow-left']").click()
            # 获取年月标签元素
            element = self.find_element(By.CLASS_NAME, "el-icon-d-arrow-left")
            # 获取标签的年
            now_year = element.get_attribute('innerText')[0:4]
        # 获取年月标签元素
        element = self.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
        # 获取标签的月
        if element.get_attribute('innerText')[8:9] == " ":
            now_month = element.get_attribute('innerText')[7:8]
        else:
            now_month = element.get_attribute('innerText')[7:9]
        # 寻找目标的月
        while month > int(now_month):
            self.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-arrow-right']").click()
            # 获取年月标签元素
            element = element = self.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
            # 获取标签的月
            if element.get_attribute('innerText')[8:9] == " ":
                now_month = element.get_attribute('innerText')[7:8]
            else:
                now_month = element.get_attribute('innerText')[7:9]
        while month < int(now_month):
            self.find_element(By.XPATH, "//Button[@class='el-picker-panel__icon-btn el-icon-arrow-left']").click()
            # 获取年月标签元素
            element = self.find_element(By.XPATH, "//div[1]/div/div[1]/div/div[contains(text(), '年')]")
            # 获取标签的月
            if element.get_attribute('innerText')[8:9] == " ":
                now_month = element.get_attribute('innerText')[7:8]
            else:
                now_month = element.get_attribute('innerText')[7:9]
        # 点击目标的日
        self.find_element(By.XPATH, "//tr/td/div/span[contains(text(), '20')]").click()

    # def
    # 滑动条操作

    # def
    # js操作

    def open_message(self):
        """
        打开消息
        :return:
        """

    def get_element_innerText(self, element):
        """
        获取标签内的文本
        :param element:
        :return:
        """
        return element.get_attribute('innerText')

    def into_menu(self, parent, children=None):
        """
        进入二级菜单
        :param parent: 一级菜单
        :param children: 二级菜单
        :return: 进入二级菜单页
        """
        if children is None:
            self.find_element_by_text(parent).click()
        else:
            pElement = self.find_element_by_text(parent)
            ActionChains(self.driver).move_to_element(pElement).perform()
            cElement = self.find_element_by_text(children)
            self.driver.execute_script("arguments[0].click();", cElement)
        sleep(5)
        return self.driver.current_url


if __name__ == '__main__':
    pass
