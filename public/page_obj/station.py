# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage

webElement = read_yamlData(r"\public\webElement\cpip.yaml")


class Station(BasePage):
    """
    临床药师智慧平台页面
    """
    # _base_url = "http://172.16.0.166:8034/index.html#/loginStation"

    def module_click(self, module):
        """
        点击进入处方点评/用户管理模块
        :return:
        """
        global element
        actions = ActionChains(self._driver)
        if module == '处方点评':
            element = self.find(webElement["cfdpModule"])
            actions.move_to_element(element).perform()
            element.click()
            sleep(2)
            from public.page_obj.main import Main
            return Main(self._driver)
        elif module == "系统管理":
            element = self.find(webElement["yhglModule"])
            actions.move_to_element(element).perform()
            element.click()
            sleep(2)
            from public.page_obj.xtgl import Xtgl
            return Xtgl(self._driver)

    def logout(self, isLogin):
        """
        退出登录操作
        """
        self.find(webElement["UserImage"]).click()
        self.find(webElement["Logout"]).click()
        self.find(webElement[isLogin]).click()
        if isLogin == "LogoutY":
            from public.page_obj.login import Login
            return Login(self._driver)
        else:
            return Station(self._driver)


if __name__ == '__main__':
   pass