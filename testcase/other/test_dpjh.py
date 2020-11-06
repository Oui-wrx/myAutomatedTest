# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from public.models.read_yaml_data import read_yamlData
from public.page_obj.dpjhPage import DpjhPage
from public.page_obj.main import Main

plan_type = [1, 2]
planName = ["天上人间", "抗菌药物点评"]
my_plan = read_yamlData(r"\testcase\testdata\myplan.yaml")
look_name = read_yamlData(r"\testcase\testdata\planName.yaml")


@allure.feature("点评计划列表页测试用例")
class Test_dpjh:
    def setup(self):
        self.dpjhPage = Main().goto_dpjh()

    def teardown(self):
        self.dpjhPage.get_driver().quit()

    @allure.story("计划搜索")
    @pytest.mark.parametrize("name", planName)
    def test_search_by_keywords(self, name):
        self.dpjhPage.search_by_keywords(name)
        if name == "抗菌药物点评":  # 存在的计划
            pytest.assume(self.dpjhPage.is_exist_plan(name), "按关键字搜索计划有问题")
        if name == "天上人间":  # 不存在的计划
            pytest.assume(self.dpjhPage.is_exist_plan(name) == False, "按关键字搜索计划有问题")

    @allure.story("新增计划")
    @pytest.mark.parametrize("planDetail", my_plan)
    def test_add_mzPlan(self, planDetail):
        self.dpjhPage.edit_new_mzPlan(planDetail)
        assert self.dpjhPage.is_exist_plan(my_plan[planDetail]["计划名称"]), "新建计划失败"

    # @allure.story("复制计划")
    # @pytest.mark.parametrize("planName", look_name)
    # def test_copy_plan(self, planName):
    #     self.dpjhPage.look_plan(planName)
    #     # assert  保存成功  列表页有复制成功的计划

    # @allure.story("计划抽取")
    # def test_exPlan(self, go_login):
    #     driver = go_login
    #     dpjh_p = DpjhPage(driver)
    #     dpjh_p.plan_extract()

    @allure.story("计划删除")
    @pytest.mark.parametrize("planName", look_name[1:])
    def test_deletePlan(self, planName):
        self.dpjhPage.delete_plan(planName)
        assert self.dpjhPage.is_exist_plan(planName) == False, "删除计划失败"


if __name__ == '__main__':
    pass
