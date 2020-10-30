# -*- coding: utf-8 -*-
# @Author : wrx

import allure
import pytest

from public.models.read_yaml_data import read_yamlData
from public.page_obj.cpipPage import CpipPage

moduleData = read_yamlData(r"\testcase\testdata\module_data.yaml")
isLogout = ["LogoutN", "LogoutY"]


@allure.feature("临床药师智慧平台测试用例")
class Test_Cpip:
    """
    临床药师智慧平台
    """
    @allure.story("模块点击测试")
    @pytest.mark.parametrize("module", moduleData)
    def test_select_module(self, module, driver):
        cpipp = CpipPage(driver)
        cpipp.module_click(module)
        if module == '处方点评':
            allure.attach("点击处方点评", attachment_type=allure.attachment_type.TEXT)
            assert driver.current_url == "http://172.16.0.166:8034/index.html#/home", "无法正常进入处方点评模块"
        else:
            allure.attach("点击系统管理", attachment_type=allure.attachment_type.TEXT)
            # driver.save_screenshot('路径')  // 保存截图
            pytest.assume(driver.current_url == "http://172.16.0.166:8034/index.html#/permissionSetting", "无法正常进入系统管理模块")
            # allure.attach.file("./aa.png", attachment_type=allure.attachment_type.PNG)  // 报告附加截图

    @allure.story("退出登录测试")
    @pytest.mark.parametrize("logout", isLogout)
    def test_logout(self, logout, driver):
        cpipp = CpipPage(driver)
        cpipp.logout(logout)
        if logout == 'LogoutY':
            pytest.assume(driver.current_url == 'http://172.16.0.166:8034/index.html#/login', "退出登录失败")
        else:
            pytest.assume(driver.current_url == 'http://172.16.0.166:8034/index.html#/loginStation', "取消登录失败, 页面有跳转")
            pytest.assume(driver.find_element("xpath", "//span[contains(text(),'取消')]"), "取消登录失败，弹框未消失")


if __name__ == "__main__":
    pass
