# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from public.models.myunit import MyUnit
from public.models.read_yaml_data import read_yamlData

menuData1 = read_yamlData(r"\testcase\testdata\menu_data.yaml")
menuData2 = read_yamlData(r"\testcase\testdata\menu_data2.yaml")
isLogout = ["LogoutN", "LogoutY"]


@allure.feature("首页测试用例")
class Test_mainPage(MyUnit):
    """
    用例描述：处方点评首页
    """

    @allure.story("测试菜单点击1")
    @pytest.mark.parametrize("menu", menuData1)
    def test_intoMenu(self, menu):
        pytest.assume(self.main.into_menu(*menu.split('-')) == menuData1[menu], "")

    @allure.story("测试菜单点击2")
    @pytest.mark.parametrize("menu", menuData2)
    def test_intoMenu2(self, menu):
        pytest.assume(self.main.into_menu(*menu.split('-')) == menuData1[menu], "")

    @allure.story("回到临床药学智慧平台")
    def test_goto_station(self):
        assert self.main.goto_station().get_driver().current_url == "http://172.16.0.166:8034/index.html#/loginStation"

    @allure.story("退出登录测试")
    @pytest.mark.parametrize("logout", isLogout)
    def test_logout(self, logout):
        if logout == "LogoutY":  # 确定退出
            self.main.click_confirm()
            sleep(3)
            pytest.assume(self.main.log_out(logout).on_page("http://172.16.0.166:8034/index.html#/login"), "退出登录失败")
        else:  # 取消退出
            self.main.click_cancell()
            sleep(3)
            pytest.assume(self.main.log_out(logout).on_page("http://172.16.0.166:8034/index.html#/home"), "取消登录失败")
            pytest.assume(self.main.log_out(logout).find_element("xpath", "//span[contains(text(),'取消')]"), "取消登录失败，弹框未消失")


if __name__ == '__main__':
    pass
