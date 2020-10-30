# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage

webElement = read_yamlData(r"\public\webElement\cpip.yaml")


class CpipPage(BasePage):
    """
    临床药师智慧平台页面
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/loginStation")
        sleep(3)

    def module_click(self, module):
        """
        点击进入处方点评/用户管理模块
        :return:
        """
        global element
        actions = ActionChains(self.driver)
        if module == '处方点评':
            element = self.find_element(webElement["cfdpModule"])
        elif module == "系统管理":
            element = self.find_element(webElement["yhglModule"])
        actions.move_to_element(element).perform()
        element.click()
        sleep(2)

    def logout(self, isLogin):
        """
        退出登录操作
        """
        self.find_element(webElement["UserImage"]).click()
        self.find_element(webElement["Logout"]).click()
        self.find_element(webElement[isLogin]).click()


if __name__ == '__main__':
    print(webElement)
