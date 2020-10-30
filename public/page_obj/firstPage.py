# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep

from selenium.webdriver import ActionChains

from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage

webElement = read_yamlData(r"\public\webElement\index.yaml")
menuElement = read_yamlData(r"\public\webElement\menu.yaml")
menuData = read_yamlData(r"\testcase\testdata\menu_data.yaml")


class FirstPage(BasePage):
    """
    处方点评首页
    # """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/home")
        sleep(2)

    # def page_check(self):
    #     """
    #     页面检查
    #     :return:
    #     """

    # def into_menu(self, parent, children=None):
    #     """
    #     进入菜单
    #     :param parent: 一级菜单
    #     :param children: 二级菜单
    #     :return:
    #     """
    #     if children is None:
    #         self.find_element(menuElement[parent]).click()
    #     else:
    #         pElement = self.find_element(menuElement[parent])
    #         sleep(2)
    #         ActionChains(self.driver).move_to_element(pElement).perform()
    #         cElement = self.find_element(menuElement[children])
    #         self.execute_script_click(cElement)
    #     sleep(3)
    #     return self.driver.current_url

    def into_menu(self, parent, children):
        if children == "无":
            self.find_element(menuElement[parent]).click()
        else:
            # pElement = \
            self.find_element(menuElement[parent]).click()
            # ActionChains(self.driver).move_to_element(pElement).perform()
            cElement = self.find_element(menuElement[children])
            # self.execute_script_click(cElement)
            cElement.click()
        sleep(3)
        return self.driver.current_url

    def go_cpipPage(self):
        """
        回到临床药师智慧平台
        :return:
        """
        self.find_element(webElement["Home"]).click()

    def log_out(self, isLogout):
        """
        退出登录操作
        """
        self.find_element(webElement["UserImage"]).click()
        self.find_element(webElement["Logout"]).click()
        if isLogout is "LogoutY":
            self.click_confirm()
        if isLogout is "LogoutN":
            self.click_cancell()


if __name__ == '__main__':
    print(menuData)
    # print(menuData.keys())
    # print(list(menuData.keys()))
    # print(list(menuData.keys())[1])
    # print(list(menuData.keys())[1].split('-'))
    # print(*list(menuData.keys())[1].split('-'))