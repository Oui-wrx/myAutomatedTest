# -*- coding: utf-8 -*-
# @Author : wrx

import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.gVariable import planTaskName
from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage
from public.page_obj.mzPlanPage import PlanPage

webElement = read_yamlData(r"\public\webElement\dpjh.yaml")


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
        return self.get_page_source()

    def goto_add_plan(self):
        """
        新增计划
        :return:
        """
        self.find(webElement["新增计划"]).click()
        return PlanPage()

    def edit_new_plan(self):
        """
        编辑新计划
        """
        plan = self.goto_add_plan()
        plan.inputPlanName("新计划")
        plan.inputPlanDescription("开始我的计划")
        plan.inputExRandom(20, '份数')
        plan.savePlan()
        plan.cancellPlan()
        sleep(5)

    def look_plan(self, planName):
        """
        查看计划详情
        :return:
        """
        self.find_element_by_text(planTaskName).click()

    def copy_plan(self):
        """
        复制计划
        :return:
        """
        self.look_plan("planTaskName")
        self.find_element_by_text("复制计划").click()
        print("********************************")
        print(self.find_element_by_text("复制计划"))
        self.find_element(*self.mz_plan_name_loc).send_keys(str(planTaskName)+"-复制计划")
        self.find_element_by_text("保存").click()
        # self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[5]/button[2]").click()
        self.find_element_by_text("取消").click()

    def modify_plan(self):
        """
        修改计划
        :return:
        """

    def plan_extract(self):
        """
        列表页抽取计划
        :return:
        """
        self.look_plan(planTaskName)
        self.find_element_by_text("抽取").click()
        sleep(3)
        # 通过属性定位时间选择器
        element = self.find_element(By.CSS_SELECTOR, "input[placeholder='开始日期']")
        print("*********************************************")
        print(self.get_element_innerText(element).strip())
        if self.get_element_innerText(element).strip() == "":
            print("为什么会进来这里呢？")
            element.click()
            sleep(5)
            self.set_calendar(2020, 6, 20)
            self.set_calendar(2020, 8, 20)
        self.find_element(By.XPATH, "//div[@class='el-dialog__footer']/span/button[@class='el-button "
                                    "el-button--primary']").click()
        sleep(3)

    def delete_plan(self):
        """
        删除计划
        :return:
        """
        self.look_plan(planTaskName)
        self.find_element_by_text("删除").click()
        # self.find_element_by_text("确定").click()
        # 弹框所有的删除 都  /html/body/div[3]/div/div[3]/button[2]/span
        self.find_element(By.CSS_SELECTOR, "body > div.w-message-box__wrapper > div > div.w-message-box__btns > "
                                           "button.w-button.w-button--default.w-button--small.w-button--primary > "
                                           "span").click()


if __name__ == '__main__':
    pass
