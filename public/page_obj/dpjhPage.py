# -*- coding: utf-8 -*-
# @Author : wrx

import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.gVariable import planTaskName
from public.page_obj.basePage import BasePage


class DpjhPage(BasePage):
    """
    点评计划列表页面
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/ReviewPlan/selectPlan")
        sleep(2)

    # 新建计划类型元素
    add_mz_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div/div[2]/div/div[1]")
    add_zy_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div/div[2]/div/div[2]")
    # 新建门诊计划元素
    mz_plan_name_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[1]/div/div[1]/div/input")
    mz_plan_description_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[1]/div/div[2]/div/textarea")
    mz_extract_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input")
    # 关于设置单次计划的时间
    # 方式一 : 直接输入
    mz_plan_fre_begin_loc = (
        "xpath", "//*[@id='app']/div/section/main/div/div[3]/div/div/div[2]/div[3]/div[2]/input[1]")
    mz_plan_fre_end_loc = ("xpath", "//*[@id='app']/div/section/main/div/div[3]/div/div/div[2]/div[3]/div[2]/input[2]")

    # 新建住院计划元素

    def page_check(self):
        """
        页面检查
        :return:
        """

    def search_my_plan(self):
        """
        全部计划和我的计划筛选
        :return:
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

    def search_keywords(self):
        """
        关键字查询
        :return:
        """

    def add_plan(self):
        """
        新增计划
        :return:
        """
        self.find_element_by_text("新增计划").click()
        self.find_element(*self.add_mz_loc).click()
        sleep(3)
        self.find_element(*self.mz_plan_name_loc).send_keys(planTaskName)
        self.find_element(*self.mz_plan_description_loc).send_keys("^^计划描述")
        self.find_element(*self.mz_extract_loc).send_keys(20)

        # 日历弹框
        self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[3]/div/div/div[2]/div[3]/div["
                                    "2]/input[1]").click()
        self.set_calendar(2020, 6, 20)
        self.set_calendar(2020, 8, 20)

        # print("******************************************************")
        # number = 0
        # for x in self.find_elements(By.TAG_NAME, "input"):
        #     number = number + 1
        #     print(x)
        # print(number)

        # 保存
        sleep(5)
        self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[5]/button[2]").click()

        # 取消
        self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[5]/button[1]").click()

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
