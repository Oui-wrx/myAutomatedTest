# -*- coding: utf-8 -*-
# @Author : wrx
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage

webElement = read_yamlData(r"\public\webElement\exResult.yaml")


class ExResultsPage(BasePage):
    """
    抽取结果列表页
    """

    def at_page(self):
        # 后期拆分 Url
        self._driver.get("http://172.16.0.166:8034/index.html#/ReviewPlan/extractResults")

    def search_by_keywords(self, name):
        """
        根据关键字搜索
        """
        self.find(webElement["输入计划名称"]).clear()
        self.find(webElement["输入计划名称"]).send_keys(name)
        self.find(webElement["搜索"]).click()

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

    def openExResult(self, planName):
        """
        查看某抽取结果
        :return:
        """
        s = "//div[text()='" + str(planName) + "']"
        try:
            self._driver.find_element(By.XPATH, s).click()
        except Exception:
            print("抽取结果打开失败")

#     def search_by_creater(self):
#         """
#         通过创建人创建计划
#         :return:
#         """
#
#     def search_by_keywords(self):
#         """
#         通过关键字搜索
#         :return:
#         """
#
#     def generateDpTask(self):
#         self.openExResult()
#         sleep(3)
#         # 点击生成点评任务
#         self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[2]/div[2]/button[2]').click()
#         sleep(3)
#         # 点击确定
#         self.find_element(By.XPATH,
#                           "//span[@class='dialog-footer']/Button[@class='el-button el-button--primary']").click()
