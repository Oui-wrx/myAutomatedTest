# -*- coding: utf-8 -*-
# @Author : wrx

import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from config.gVariable import planTaskName
from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage
from public.page_obj.mzPlanPage import MzPlanPage

webElement = read_yamlData(r"\public\webElement\dpjh.yaml")

myPlan = read_yamlData(r"\testcase\testdata\myplan.yaml")


class DpjhPage(BasePage):
    """
    点评计划列表页面
    """

    def search_by_type(self):
        """
        计划类型筛选
        :return:
        """

    def search_by_creator(self):
        """
        创建人筛选
        :return:
        """

    def search_by_keywords(self, name):
        """
        根据关键字搜索
        """
        self.find(webElement["输入计划名称"]).clear()
        self.find(webElement["输入计划名称"]).send_keys(name)
        self.find(webElement["搜索"]).click()
        sleep(8)

    def is_exist_plan(self, planName):
        """
        是否存在某计划, 在搜索计划的基础上
        """
        self.search_by_keywords(planName)
        s = "//div[text()='" + str(planName) + "']"
        print(s)
        try:
            if self._driver.find_element(By.XPATH, s):
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def goto_add_plan(self, type):
        """
        新增计划
        :return:
        """
        self.find(webElement["新增计划"]).click()
        if type == "门诊计划":
            self.find(webElement["门急诊处方点评"]).click()
            return MzPlanPage(self._driver)
        else:
            self.find(webElement["住院医嘱点评"]).click()
            return MzPlanPage(self._driver)

    def edit_new_mzPlan(self, planDetail):
        """
        编辑新门诊计划
        """
        print(planDetail)
        plan = self.goto_add_plan(myPlan[planDetail]["计划类型"])
        plan.inputPlanName(myPlan[planDetail]["计划名称"])
        plan.inputPlanDescription(myPlan[planDetail]["计划描述"])
        print(myPlan[planDetail]["抽取方式"][4:6])
        print(myPlan[planDetail]["抽取方式"][6:])
        plan.inputExRandom(myPlan[planDetail]["抽取方式"][4:6], myPlan[planDetail]["抽取方式"][6:7])
        if myPlan[planDetail]["动作"] == '保存':
            sleep(3)
            self.scroll_page("down")
            plan.savePlan()
            sleep(4)
        return DpjhPage(self._driver)

    def look_plan(self, planName):
        """
        点击计划，查看计划详情
        :return:
        """
        s = "//div[text()='" + str(planName) + "']"
        print(s)
        self._driver.find_element(By.XPATH, s).click()
        sleep(5)

    # def copy_plan(self, planName):
    #     """
    #     复制计划
    #     :return:
    #     """
    #     self.look_plan(planName)
    #     self.find(webElement["复制计划"]).click()
    #     print("********************************")
    #     print(self.find_element_by_text("复制计划"))
    #     self.find_element(*self.mz_plan_name_loc).send_keys(str(planTaskName)+"-复制计划")
    #     self.find_element_by_text("保存").click()
    #     # self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[5]/button[2]").click()
    #     self.find_element_by_text("取消").click()
    #
    # def modify_plan(self):
    #     """
    #     修改计划
    #     :return:
    #     """
    #
    # def plan_extract(self):
    #     """
    #     列表页抽取计划
    #     :return:
    #     """
    #     self.look_plan(planTaskName)
    #     self.find_element_by_text("抽取").click()
    #     sleep(3)
    #     # 通过属性定位时间选择器
    #     element = self.find_element(By.CSS_SELECTOR, "input[placeholder='开始日期']")
    #     print("*********************************************")
    #     print(self.get_element_innerText(element).strip())
    #     if self.get_element_innerText(element).strip() == "":
    #         print("为什么会进来这里呢？")
    #         element.click()
    #         sleep(5)
    #         self.set_calendar(2020, 6, 20)
    #         self.set_calendar(2020, 8, 20)
    #     self.find_element(By.XPATH, "//div[@class='el-dialog__footer']/span/button[@class='el-button "
    #                                 "el-button--primary']").click()
    #     sleep(3)

    def delete_plan(self, planName):
        """
        删除计划   目前是确定删除  后期扩展取消删除
        :return:
        """
        self.scroll_page("right")
        self.search_by_keywords(planName)
        sleep(4)
        self.look_plan(planName)
        self.scroll_page("down")
        self.find(webElement["删除"]).click()
        self.click_confirm()
        sleep(4)


if __name__ == '__main__':
    pass
