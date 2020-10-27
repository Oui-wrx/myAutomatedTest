# -*- coding: utf-8 -*-
# @Author  : wrx


import allure

import ddt
import pytest

from public.models.myunit import MyUnit
from public.models.read_yaml_data import read_yaml_data
from public.page_obj.loginPage import LoginPage

testData = read_yaml_data(r"\testdata\login_data.yaml")
testElement = read_yaml_data(r"\testelement\login.yaml")


@ddt.ddt
@allure.feature("测试登录模块")
class Test_login(MyUnit):
    """
    登录测试
    """
    @ddt.data(*testData)
    @allure.story('登录测试用例')
    def test_login(self, data):
        lp = LoginPage(self.driver)
        with allure.step("开始登录"):
            lp.login(data['data']['username'], data['data']['password'])
        if data['data']['username'] == "" or data['data']['password'] == "":

            assert lp.find_element("xpath", "//p[contains(text(), '警告，用户名或密码为空')]")
        if lp.no_exist_user_hint() == "用户名不存在":
            lp.click_ok_close()
        if lp.user_pwd_err_hint() == "密码和用户名不匹配":
            lp.click_ok_close()


if __name__ == "__main__":
    pass
