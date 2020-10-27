# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage


class FirstPage(BasePage):
    """
    处方点评首页
    # """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/home")
        sleep(3)

    # 页面元素
    home_loc = ("xpath", '//*[@id="app"]/div/header/div/div[1]/div/div[2]/span/i')  # 小房子标识
    user_img_loc = ("xpath", '//*[@id="app"]/div/header/div/div[1]/div/div[2]/div/span')  # 用户头像标识

    def page_check(self):
        """
        页面检查
        :return:
        """
        top_element = self.find_elements("xpath", "//li")
        top_text = []
        for element in top_element:
            top_text.append(element.get_attribute('innerText'))
        top_text = ''.join(top_text)
        # 管理员所需模块
        need_text = ["首页", "计划管理", "点评计划", "抽取结果", "点评工作", "门急诊处方点评", "住院医嘱点评", "结果公示", "配置", "退出登录"]
        print(top_text)
        # 模块检查
        for need_t in need_text:
            if need_t in top_text:
                print("**************************************************************")
                continue
            else:
                return False
        return True

    def log_out(self):
        """
        退出登录
        :return:
        """
        self.find_element(*self.user_img_loc).click()
        # 点击退出登录
        self.find_element_by_text("退出登录").click()
        sleep(5)

    def go_home(self):
        """
        回到临床药师智慧平台
        :return:
        """
        self.find_element(*self.home_loc).click()


if __name__ == '__main__':
    pass
