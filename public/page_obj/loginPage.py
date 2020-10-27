# -*- coding: utf-8 -*-
# @Author  : wrx

from time import sleep
from public.page_obj.basePage import BasePage
from public.models.read_yaml_data import read_yaml_data

loginElement = read_yaml_data(r"\testelement\login.yaml")


class LoginPage(BasePage):
    """
    用户登录页面
    """

    def __init__(self, driver):
        super().__init__(driver)
        # self.open()

    # 元素属性定位元素对象
    # 账号输入框  By.ID userName
    login_user_loc = (loginElement[0]["find_type"], loginElement[0]["element_info"])
    # 密码输入框
    login_password_loc = (loginElement[1]["find_type"], loginElement[1]["element_info"])
    # 记住本次登录
    remember_login_loc = (loginElement[2]["find_type"], loginElement[2]["element_info"])
    # 点击登录
    login_btn_loc = (loginElement[3]["find_type"], loginElement[3]["element_info"])

    def login_input_user(self, username):
        """
        账号输入
        :param username:
        :return:
        """
        self.find_element(*self.login_user_loc).clear()
        self.find_element(*self.login_user_loc).send_keys(username)

    def login_input_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    def remember_login(self):
        """
        记住本次登录
        :return:
        """
        self.find_element(*self.remember_login_loc).click()

    def login_btn_click(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_btn_loc).click()

    def login_exit(self):
        """
        退出系统  ??
        :return:
        """
        self.find_element(*self.login_exit_loc).click()

    def login(self, username, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.login_input_user(username)
        self.login_input_password(password)
        self.remember_login()
        self.login_btn_click()
        sleep(2)

    # 用户不存在
    no_exist_user_loc = (loginElement[6]["find_type"], loginElement[6]["element_info"])
    # 用户或密码为空
    no_user_pwd_err_loc = (loginElement[7]["find_type"], loginElement[7]["element_info"])
    # 用户密码不匹配
    user_pwd_err_loc = (loginElement[8]["find_type"], loginElement[8]["element_info"])
    # 点击用户头像
    info_usr_loc = (loginElement[4]["find_type"], loginElement[4]["element_info"])
    # 退出登录
    login_exit_loc = (loginElement[5]["find_type"], loginElement[5]["element_info"])

    # 用户不存在提示
    def no_exist_user_hint(self):
        if self.find_element(*self.no_exist_user_loc):
            return self.find_element(*self.no_exist_user_loc).text
        else:
            return 0

    # 用户密码不匹配
    def user_pwd_err_hint(self):
        if self.find_element(*self.user_pwd_err_loc):
            return self.find_element(*self.user_pwd_err_loc).text
        else:
            return 0


if __name__ == '__main__':
    pass