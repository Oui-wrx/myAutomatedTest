# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage
from public.page_obj.dpjhPage import DpjhPage
from public.page_obj.login import Login
from public.page_obj.station import Station

webElement = read_yamlData(r"\public\webElement\index.yaml")
menuElement = read_yamlData(r"\public\webElement\menu.yaml")
menuData = read_yamlData(r"\testcase\testdata\menu_data.yaml")


class Main(BasePage):
    """
    处方点评首页
    """

    _base_url = "http://172.16.0.166:8034/index.html"

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        if self._driver.current_url == 'http://172.16.0.166:8034/index.html#/login':
            Login(self._driver).login("admin", "123").module_click("处方点评")

    def into_menu(self, parent, children):
        self.find(menuElement["首页"]).click()
        if children == "无":
            self.find(menuElement[parent]).click()
        else:
            # self.find(menuElement[parent]).click()
            pElement = self.find(menuElement[parent])
            print(self.find(menuElement[parent]).text)
            ActionChains(self._driver).move_to_element(pElement).perform()
            sleep(2)
            cElement = self.find(menuElement[children])
            # print(self.find(menuElement[children]).text)
            cElement.click()
        sleep(3)
        return self._driver.current_url

    def goto_station(self):
        """
        回到临床药师智慧平台
        :return:
        """
        sleep(4)
        self.find(webElement["Home"]).click()
        return Station(self._driver)

    def log_out(self, isLogout):
        """
        退出登录操作
        """
        self.find(webElement["UserImage"]).click()
        self.find(webElement["Logout"]).click()
        if isLogout is "LogoutY":
            self.click_confirm()
            return Login()
        if isLogout is "LogoutN":
            self.click_cancell()
            return Main(self._driver)

    def goto_dpjh(self):
        self.into_menu("计划管理", "点评计划")
        # elements = self._driver.find_elements(By.CSS_SELECTOR, 'el-submenu__title')
        # for ele in elements:
        #     if "计划管理" in ele.text:
        #         # ele.click()
        #         ActionChains(self._driver).move_to_element(ele).perform()
        return DpjhPage(self._driver)

    def ss(self):   # 测试函数
        # c = self._driver.find_element_by_xpath("//div['计划管理' in @text()]")
        # c = self._driver.find_element_by_css_selector('#app > div > header > div > div > div > ul > li:nth-child(5)')
        eles = self._driver.find_elements_by_css_selector('.el-submenu__title')
        for ele in eles:
            print(ele.text)
            if "点评工作" in ele.text:    # 计划管理->点评工作  点评工作->结果公示->  点评结果->哪也不去
                ActionChains(self._driver).move_to_element(ele).perform()
            else:
                # print("定位错误")
                pass
        sleep(5)


if __name__ == '__main__':
    # Main().log_out("LogoutY")
    Main().ss()
