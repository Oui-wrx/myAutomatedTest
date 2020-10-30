# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from public.models.read_yaml_data import read_yamlData
from public.page_obj.firstPage import FirstPage
from public.page_obj.loginPage import LoginPage

menuData1 = read_yamlData(r"\testcase\testdata\menu_data.yaml")
menuData2 = read_yamlData(r"\testcase\testdata\menu_data2.yaml")
isLogout = ["LogoutN", "LogoutY"]


@allure.feature("首页测试用例")
class Test_firstPage:
    # class Test_firstPage(MyUnit):
    """
    用例描述：处方点评首页
    """

    @allure.story("测试菜单点击1")
    @pytest.mark.parametrize("menu", menuData1)
    def test_intoMenu(self, menu, driver):
        first_p = FirstPage(driver)
        print(menu, menuData1[menu])
        # allure.attach(str(menu)+menuData1[menu], attachment_type = allure.attachment_type.TEXT)
        pytest.assume(first_p.into_menu(*menu.split('-')) == menuData1[menu], "")

    @allure.story("测试菜单点击2")
    @pytest.mark.parametrize("menu", menuData2)
    def test_intoMenu2(self, menu, driver):
        first_p = FirstPage(driver)
        driver.refresh()
        print(menu, menuData2[menu])
        # allure.attach(str(menu) + menuData1[menu], attachment_type=allure.attachment_type.TEXT)
        pytest.assume(first_p.into_menu(*menu.split('-')) == menuData2[menu], "")

    @allure.story("回到临床药学智慧平台")
    def test_go_cpip(self, driver):
        first_p = FirstPage(driver)
        first_p.go_cpipPage()
        sleep(3)
        assert driver.current_url == "http://172.16.0.166:8034/index.html#/loginStation"

    @allure.story("退出登录测试")
    @pytest.mark.parametrize("logout", isLogout)
    def test_logout(self, logout, driver):
        first_p = FirstPage(driver)
        first_p.log_out(logout)
        if logout == "LogoutY":  # 确定退出
            first_p.click_confirm()
            sleep(3)
            pytest.assume(first_p.on_page("http://172.16.0.166:8034/index.html#/login"), "退出登录失败")
            LoginPage(driver).login("admin", "123")  # 防止测试停止
        else:  # 取消退出
            first_p.click_cancell()
            sleep(3)
            pytest.assume(driver.current_url == "http://172.16.0.166:8034/index.html#/home", "取消登录失败")
            pytest.assume(driver.find_element("xpath", "//span[contains(text(),'取消')]"), "取消登录失败，弹框未消失")


if __name__ == '__main__':
    pass
