# -*- coding: utf-8 -*-
# @Author : wrx

import allure
import pytest

from public.models.read_yaml_data import read_yamlData
from public.page_obj.login import Login
from public.page_obj.main import Main
webElement = read_yamlData(r"\public\webElement\index.yaml")
webElement2 = read_yamlData(r"\public\webElement\xtgl.yaml")
webElement3 = read_yamlData(r"\public\webElement\login.yaml")

moduleData = read_yamlData(r"\testcase\testdata\module_data.yaml")
isLogout = ["LogoutN", "LogoutY"]


@allure.feature("临床药师智慧平台测试用例")
class Test_Station:
    """
    临床药师智慧平台
    """
    def setup(self):
        self.stationPage = Login().login("admin", "123")

    def teardown(self):
        self.stationPage.get_driver().quit()

    @allure.story("模块点击测试")
    @pytest.mark.parametrize("module", moduleData)
    def test_select_module(self, module):
        if module == '处方点评':
            allure.attach("点击处方点评", attachment_type=allure.attachment_type.TEXT)
            assert self.stationPage.module_click(module).find(webElement["Home"])
        else:
            allure.attach("点击系统管理", attachment_type=allure.attachment_type.TEXT)
            # driver.save_screenshot('路径')  // 保存截图
            # allure.attach.file("./aa.png", attachment_type=allure.attachment_type.PNG)  // 报告附加截图
            assert self.stationPage.module_click(module).find(webElement2["Home"])

    @allure.story("退出登录测试")
    @pytest.mark.parametrize("logout", isLogout)
    def test_logout(self, logout):
        if logout == 'LogoutY':
            assert self.stationPage.logout(logout).find(webElement3["UserName"])
        else:
            pytest.assume("确定要退出登录" in self.stationPage.logout(logout).get_page_source())
            pytest.assume("临 床 药 学 智 慧 平 台" in self.stationPage.logout(logout).get_page_source())


if __name__ == "__main__":
    pass
