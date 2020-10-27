#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 10:00
# @Author  : wrx
# @FileName: driver.py
# @Software: PyCharm

from selenium import webdriver

# url = 'http://172.16.0.166:8034/index.html'
#
#
# # 返回登录入口
# def WDriver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)
#     return driver


class WDriver:

    def chromeDriver(self):
        """
        chrome driver
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    # Firefox driver
    # def

    # Ie driver
    # def


if __name__ == '__main__':
    WDrive = WDriver()
    WDrive.chromeDriver()
