# -*- coding: utf-8 -*-
# @Author : wrx
import allure
import pytest

from public.models.myunit import MyUnit
from public.page_obj.cpipPage import CpipPage


@allure.feature("临床药师智慧平台测试用例")
class Test_Cpip:

    @allure.story("进入处方点评模块测试")
    def test_select_cfdp_module(self, go_login):
        """
        测试进入处方点评模块
        :return:
        """
        cpipp = CpipPage(go_login)
        cpipp.cfdp_module_click("处方点评")

    @allure.testcase("http://172.16.0.166:8034/index.html#/permissionSetting")
    @allure.story("进入系统管理模块测试")
    def test_select_yhgl_module(self, go_login):
        """
        测试进入用户管理模块
        :return:
        """
        cpipp = CpipPage(go_login)
        with allure.step("点击系统管理"):
            cpipp.cfdp_module_click("系统管理")
        with allure.step("保存图片"):
            go_login.save_screenshot("./aa.png")
            allure.attach.file("./aa.png", attachment_type=allure.attachment_type.PNG)

    @allure.story("退出登录测试")
    def test_logout(self, go_login):
        """
        测试退出登录
        :return:
        """
        cpipp = CpipPage( go_login)
        cpipp.logout()


if __name__ == "__main__":
    pytest.main()
