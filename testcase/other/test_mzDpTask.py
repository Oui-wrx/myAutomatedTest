# -*- coding: utf-8 -*-
# @Author : wrx
import allure
import pytest

from public.page_obj.mzDpTaskPage import MzDpTaskPage


@allure.feature("门诊点评任务列表")
class Test_mzDpTaskPage:

    # @allure.story("任务列表页面检查")
    # def test_check(self):
    #     pass

    @allure.story("打开点评任务表, 暂时的用例")
    @pytest.mark.dependency(name="openDpTaskTable", depends=["generateDpWork"], scope="package")
    def test_openDpTaskTable(self, go_login):
        driver = go_login
        mzDpTaskPage = MzDpTaskPage(driver)
        mzDpTaskPage.openDpTask(0)
