# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from config.gVariable import planTaskName
from public.page_obj.dpjhPage import DpjhPage
from public.page_obj.main import Main

plan_type = [1, 2]
planName = ["天上人间", "抗菌药物点评"]


@allure.feature("点评计划列表页测试用例")
class Test_dpjh:
    def setup(self):
        self.dpjhPage = Main().goto_dpjh()

    def teardown(self):
        self.dpjhPage.get_driver().quit()

    @allure.story("计划搜索")
    @pytest.mark.parametrize("name", planName)
    def test_search_by_keywords(self, name):
        searchResult = self.dpjhPage.search_by_keywords(name)
        if name == "抗菌药物点评":  # 存在的计划
            pytest.assume(name in searchResult, "按关键字搜索计划有问题")
        if name == "天上人间":  # 不存在的计划
            pytest.assume(name not in searchResult, "按关键字搜索计划有问题")

    @allure.story("新增计划")
    # @pytest.mark.parametrize("type", plan_type)
    def test_add_plan(self, go_login):
        driver = go_login
        dpjh_p = DpjhPage(driver)
        dpjh_p.add_plan()
        # assert  保存成功   列表页有计划

    @allure.story("复制计划")
    def test_copy_plan(self, go_login):
        driver = go_login
        dpjh_p = DpjhPage(driver)
        dpjh_p.copy_plan()
        sleep(5)
        # assert  保存成功  列表页有复制成功的计划

    @allure.story("计划抽取")
    @pytest.mark.dependency(name="exPlan", scope="package")
    def test_exPlan(self, go_login):
        driver = go_login
        dpjh_p = DpjhPage(driver)
        dpjh_p.plan_extract()

    @allure.story("计划删除")
    def test_deletePlan(self, go_login):
        driver = go_login
        dpjh_p = DpjhPage(driver)
        dpjh_p.delete_plan()


if __name__ == '__main__':
    pass
