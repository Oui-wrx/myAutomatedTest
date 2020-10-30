# -*- coding: utf-8 -*-
# @Author  : wrx

from public.page_obj.basePage import BasePage
from public.models.read_yaml_data import read_yamlData

webElement = read_yamlData(r"\public\webElement\login.yaml")


class LoginPage(BasePage):
    """
    用户登录页面
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.open()

    def login(self, username, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.find_element(webElement["UserName"]).clear()
        self.find_element(webElement["UserName"]).send_keys(username)
        self.find_element(webElement["PassWord"]).clear()
        self.find_element(webElement["PassWord"]).send_keys(password)
        self.find_element(webElement["Login"]).click()


if __name__ == '__main__':
    pass
