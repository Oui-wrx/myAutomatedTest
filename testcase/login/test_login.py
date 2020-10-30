# -*- coding: utf-8 -*-
# @Author  : wrx
from time import sleep

import allure
import pytest

from public.models.read_yaml_data import read_yamlData
from public.page_obj.loginPage import LoginPage

loginData = read_yamlData(r"\testcase\testdata\login_data.yaml")
loginFailData = loginData[0:3]
loginSuccessData = loginData[3:]


@allure.feature("测试登录模块")
class Test_login:
    """
    登录测试
    """
    @allure.story('登录失败测试用例')
    @pytest.mark.parametrize("loginData", loginFailData)
    def test_login_failure(self, loginData, driver):
        lp = LoginPage(driver)
        with allure.step("开始登录"):
            lp.login(loginData['data']['username'], loginData['data']['password'])
        if loginData['data']['username'] == "" or loginData['data']['password'] == "":
            with allure.step("用户密码或密码输入为空"):
                assert driver.find_element("xpath", "//p[contains(text(), '警告，用户名或密码为空')]"), "密码为空没有正确提示"
        if lp.find_element(loginData['data']).text == "用户名不存在":
            with allure.step("用户名不存在"):
                number = 1
            assert number == 1, "用户名不存在时，没有正确提示"
        if lp.find_element(loginData['data']).text == "密码和用户名不匹配":
            with allure.step("密码和用户名不匹配"):
                number = 2
            assert number == 2, "用户名和密码不匹配时，没有正确提示"
        # if driver.find_element(By.XPATH, "div.el-message-box__message > p").text == "索引和长度必须引用该字符串内的位置。 参数名: length":
        #     assert True, "用户密码输入错误，但是提示不合理"

    @allure.story('登录成功测试用例')
    @pytest.mark.parametrize("loginData", loginSuccessData)
    def test_login_success(self, loginData, driver):
        lp = LoginPage(driver)
        lp.login(loginData['data']['username'], loginData['data']['password'])
        sleep(2)
        assert driver.current_url == 'http://172.16.0.166:8034/index.html#/loginStation', "登陆失败"


if __name__ == "__main__":
    pass
