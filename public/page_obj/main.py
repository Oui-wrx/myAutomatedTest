# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep

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
    # _base_url = "http://172.16.0.166:8034/index.html"

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        # self.get_driver().get(self._base_url)
        self.get_driver().get("http://172.16.0.166:8034/index.html")
        if self._driver.current_url == 'http://172.16.0.166:8034/index.html#/login':
            Login(self._driver).login("admin", "123").module_click("处方点评")
    #
    # def __init__(self, driver: WebDriver = None):
    #     super().__init__(driver)
    #     self.get_driver().get("http://172.16.0.166:8034/index.html")
    #     Login(self._driver).login("admin", "123").module_click("处方点评")

    def into_menu(self, parent, children):
        if children == "无":
            self.find(menuElement[parent]).click()
        else:
            self.find(menuElement[parent]).click()
            # ActionChains(self.driver).move_to_element(pElement).perform()
            cElement = self.find(menuElement[children])
            # self.execute_script_click(cElement)
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
        return DpjhPage(self._driver)


if __name__ == '__main__':
    Main().log_out("LogoutY")
