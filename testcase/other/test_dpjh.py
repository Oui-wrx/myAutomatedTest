# -*- coding: utf-8 -*-
# @Author : wrx

import allure
import pytest

from public.models.myunit import MyUnit
from public.models.read_yaml_data import read_yamlData
from public.page_obj.dpjhPage import DpjhPage

plan_type = [1, 2]
planName = ["天上人间", "抗菌药物点评"]
my_plan = read_yamlData(r"\testcase\testdata\myplan.yaml")
look_name = read_yamlData(r"\testcase\testdata\planName.yaml")


@allure.feature("点评计划列表页测试用例")
class Test_dpjh(MyUnit):

    def setup(self):
        self.dpjhPage = DpjhPage(self.main.get_driver())
        self.dpjhPage.at_page()

    @allure.story("新增计划")
    @pytest.mark.dependency(name="add")
    @pytest.mark.parametrize("planDetail", my_plan)
    def test_add_mzPlan(self, planDetail):
        self.dpjhPage.edit_new_mzPlan(planDetail)
        assert self.dpjhPage.is_exist_plan(my_plan[planDetail]["计划名称"]), "新建计划失败"

    @allure.story("计划搜索")
    @pytest.mark.parametrize("name", planName)
    def test_search_by_keywords(self, name):
        self.dpjhPage.search_by_keywords(name)
        if name == "抗菌药物点评":  # 存在的计划
            pytest.assume(self.dpjhPage.is_exist_plan(name), "按关键字搜索计划有问题")
        if name == "天上人间":  # 不存在的计划
            pytest.assume(self.dpjhPage.is_exist_plan(name) == False, "按关键字搜索计划有问题")

    @allure.story("复制计划")
    @pytest.mark.parametrize("planType, planName, newName", [look_name[2]])
    def test_copy_plan(self, planType, planName, newName):
        self.dpjhPage.copy_plan(planType, planName, newName)
        assert self.dpjhPage.is_exist_plan(look_name[2][2]), "复制计划失败"

    @allure.story("计划抽取")
    @pytest.mark.parametrize("planName, startTime, endTime", [look_name[3]])
    def test_exPlan(self, planName, startTime, endTime):
        assert self.dpjhPage.plan_extract(planName, startTime, endTime), "计划抽取有点问题"

    @allure.story("计划删除")
    @pytest.mark.parametrize("planName", look_name[1:2])
    def test_deletePlan(self, planName):
        self.dpjhPage.delete_plan(planName)
        assert self.dpjhPage.is_exist_plan(planName) == False, "删除计划失败"

    @allure.story("计划修改")
    @pytest.mark.parametrize("planName", look_name[0:1])
    def test_modifyPlan(self, planName):
        pytest.assume("保存" in self.dpjhPage.modify_plan(planName), "修改计划有问题")


if __name__ == '__main__':
    print(look_name)
