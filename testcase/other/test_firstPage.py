# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from public.page_obj.firstPage import FirstPage
from public.page_obj.loginPage import LoginPage

logout_select = ["确定", "取消"]


@allure.feature("首页测试用例")
class Test_firstPage:
    # class Test_firstPage(MyUnit):
    """
    用例描述：处方点评首页
    """

    @allure.story("页面检查")
    def test_page_check(self, go_login):
        driver = go_login
        first_p = FirstPage(driver)
        assert first_p.page_check()

    @allure.story("回到临床药学智慧平台")
    def test_go_home(self, go_login):
        driver = go_login
        first_p = FirstPage(driver)
        first_p.go_home()
        # print(driver.current_url)
        assert "http://172.16.0.166:8034/index.html#/loginStation" == driver.current_url

    @allure.story("退出登录：是/否")
    @pytest.mark.parametrize("log_ok", logout_select)
    def test_logout(self, log_ok, go_login):
        driver = go_login
        first_p = FirstPage(driver)
        first_p.log_out()
        if log_ok == "确定":  # 确定退出
            first_p.click_ok_close()
            sleep(3)
            assert driver.current_url == "http://172.16.0.166:8034/index.html#/login"
            LoginPage(driver).login("admin", "123")
        else:  # 取消退出
            first_p.click_nok_close()
            sleep(3)
            assert driver.current_url == "http://172.16.0.166:8034/index.html#/home"

    @allure.story("菜单点击进入")
    @pytest.mark.skip(reason="用例需要修改")
    def test_intoMenu(self, go_login):
        driver = go_login
        first_p = FirstPage(driver)
        assert first_p.into_menu("首页") == "http://172.16.0.166:8034/index.html#/home"
        assert first_p.into_menu("计划管理", "点评计划") == "http://172.16.0.166:8034/index.html#/ReviewPlan/selectPlan"
        assert first_p.into_menu("计划管理", "抽取结果") == "http://172.16.0.166:8034/index.html#/ReviewPlan/extractResults"
        assert first_p.into_menu("点评工作", "门急诊处方点评") == "http://172.16.0.166:8034/index.html#/Outpatient"
        assert first_p.into_menu("点评工作", "住院医嘱点评") == "http://172.16.0.166:8034/index.html#/Review/Hospitalization"
        assert first_p.into_menu("点评结果", "点评工作表") == "http://172.16.0.166:8034/index.html#/ReviewResult/LookWorksheet"
        assert first_p.into_menu("点评结果",
                                 "门急诊处方") == "http://172.16.0.166:8034/index.html#/ReviewResult/ResultOutpatient"
        assert first_p.into_menu("点评结果", "住院病历") == "http://172.16.0.166:8034/index.html#/ResultHospitalization"
        assert first_p.into_menu("结果公示") == "http://172.16.0.166:8034/index.html#/PublicityResult"
        assert first_p.into_menu("配置") == "http://172.16.0.166:8034/index.html#/FunctionSwitch"


if __name__ == '__main__':
    pass
