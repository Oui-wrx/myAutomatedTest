# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage
from public.page_obj.loginPage import LoginPage

username = "admin"
password = "123"


class CpipPage(BasePage):
    """
    临床药师智慧平台
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/loginStation")
        sleep(2)


    # 模块元素
    cfdp_module_loc = ('xpath', "//*[@id='app']/div/div[2]/span[1]/*[name()='svg']")
    yhgl_module_loc = ('xpath', "//*[@id='app']/div/div[2]/span[2]/*[name()='svg']")

    # 头像元素
    head_img_loc = ("xpath", "//*[@id='app']/div/div[1]/div/div/div/button")

    def cfdp_module_click(self, module):
        """
        点击进入处方点评/用户管理模块
        :return:
        """
        global element
        actions = ActionChains(self.driver)
        if module == '处方点评':
            element = self.find_element(*self.cfdp_module_loc)
        elif module == "系统管理":
            element = self.find_element(*self.yhgl_module_loc)
        actions.move_to_element(element).perform()
        element.click()
        sleep(5)

    def logout(self):
        """
        退出登录
        :return:
        """
        self.find_element(*self.head_img_loc).click()
        self.find_element(By.XPATH, "//body/ul/li[1]").click()
        self.click_ok_close()


if __name__ == '__main__':
    pass
