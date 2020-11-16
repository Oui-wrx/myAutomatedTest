# -*- coding: utf-8 -*-
# @Author : wrx

from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from config.setting import base_url
from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage
from public.page_obj.exResultsPage import ExResultsPage
from public.page_obj.mzPlanPage import MzPlanPage
from public.page_obj.zyPlanPage import ZyPlanPage

webElement = read_yamlData(r"\public\webElement\dpjh.yaml")

myPlan = read_yamlData(r"\testcase\testdata\myplan.yaml")

look_name = read_yamlData(r"\testcase\testdata\planName.yaml")


class DpjhPage(BasePage):
    """
    点评计划列表页面
    """

    def at_page(self):
        # 后期分离 Url
        self._driver.get( base_url + "#/ReviewPlan/selectPlan")

    def search_by_keywords(self, name):
        """
        根据关键字搜索
        """
        self.find(webElement["输入计划名称"]).clear()
        self.find(webElement["输入计划名称"]).send_keys(name)
        self.find(webElement["搜索"]).click()
        sleep(3)
        self.take_screenshot("cdnj.png")

    def is_exist_plan(self, planName):
        """
        是否存在某计划
        目前是首页，用到的话后期扩展
        """
        s = "//div[text()='" + str(planName) + "']"
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
        # print(planDetail)
        plan = self.goto_add_plan(myPlan[planDetail]["计划类型"])
        plan.inputPlanName(myPlan[planDetail]["计划名称"])
        plan.inputPlanDescription(myPlan[planDetail]["计划描述"])
        # print(myPlan[planDetail]["抽取方式"][4:6])
        # print(myPlan[planDetail]["抽取方式"][6:])
        sleep(3)
        plan.inputExRandom(myPlan[planDetail]["抽取方式"][4:6], myPlan[planDetail]["抽取方式"][6:7])
        if myPlan[planDetail]["动作"] == '保存':
            self.scroll_page_by_js("down")
            plan.savePlan()
            plan.cancellPlan()
        # return DpjhPage(self._driver)

    def look_plan(self, planName):
        """
        点击计划，查看计划详情
        :return:
        """
        s = "//div[text()='" + str(planName) + "']"
        # print(s)
        self._driver.find_element(By.XPATH, s).click()

    def copy_plan(self, planType, planName, newName):
        """
        复制计划：待复制计划类型 --- 待复制计划名称 --- 复制后新计划名称
        """
        self.look_plan(planName)
        self.find(webElement["复制计划"]).click()
        plan = object
        if planType == "m":  # 待复制计划为门诊计划
            plan = MzPlanPage(self._driver)
        else:  # 待复制计划为住院计划
            plan = ZyPlanPage(self._driver)
        sleep(3)
        self._driver.refresh()
        plan.inputPlanName(newName)
        self.scroll_page_by_js("down")
        sleep(2)
        plan.savePlan()
        sleep(2)
        plan.cancellPlan()

    def modify_plan(self, planName):
        """
        修改计划
        :return:
        """
        self.look_plan(planName)
        self.find(webElement["修改"]).click()
        sleep(3)
        self._driver.refresh()
        self.scroll_page_by_js("down")
        return self.get_page_source()

    def plan_extract(self, planName, startTime=None, endTime=None):
        """
        列表页抽取计划
        """
        self.look_plan(planName)
        self.find(webElement["抽取"]).click()
        element = self.find(webElement["开始时间"])
        # 根据属性获取表内的value
        if element.get_attribute("value").strip() == "":
            element.click()
            self.set_calendar(*(startTime.split('-')))
            self.set_calendar(*(endTime.split('-')))
        self.find(webElement["抽取确定"]).click()
        if "请调整计划的抽取条件后再试" in self.get_page_source():
            return True
        elif "马上查看" in self.get_page_source():
            self.find(webElement["马上查看"]).click()
            sleep(3)
            if "生成点评任务" in self.get_page_source():
                return True
        else:
            return False

    def delete_plan(self, planName):
        """
        删除计划   目前是确定删除  后期扩展取消删除
        :return:
        """
        self.scroll_page_by_js("right")
        self.search_by_keywords(planName)
        sleep(2)
        self.look_plan(planName)
        self.scroll_page_by_js("down")
        self.find(webElement["删除"]).click()
        self.click_confirm()
        sleep(2)

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


if __name__ == '__main__':
    print(look_name)
    print(look_name[3])
    print(len(look_name[2]))
