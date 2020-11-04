# -*- coding: utf-8 -*-
# @Author  : wrx
import time

from selenium.webdriver.common.keys import Keys

from public.page_obj.basePage import BasePage
from public.models.read_yaml_data import read_yamlData
from public.page_obj.station import Station

webElement = read_yamlData(r"\public\webElement\login.yaml")


class Login(BasePage):
    """
    用户登录页
    """
    _base_url = "http://172.16.0.166:8034/index.html"

    def login(self, username, password):
        self.find(webElement["UserName"]).clear()
        self.find(webElement["UserName"]).send_keys(username)
        self.find(webElement["PassWord"]).clear()
        self.find(webElement["PassWord"]).send_keys(password)
        # time.sleep(3)
        # self.find(webElement["Login"]).click()
        self.find(webElement["PassWord"]).send_keys(Keys.ENTER)
        return Station(self._driver)


if __name__ == '__main__':
    login = Login()
    login.login("admin", "123")
    time.sleep(4)
    COOKIE = login.get_driver().get_cookies()
    print(COOKIE)
