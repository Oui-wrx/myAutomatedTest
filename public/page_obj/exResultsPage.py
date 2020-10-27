# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config.gVariable import planTaskName
from public.page_obj.basePage import BasePage


class ExResultsPage(BasePage):
    """
    抽取结果列表页
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/ReviewPlan/extractResults")
        # self.driver.refresh()
        sleep(2)

    def search_myplan(self):
        """
        筛选自己的计划
        :return:
        """

    def search_by_type(self):
        """
        通过计划类型筛选抽取结果
        :return:
        """

    def search_by_creater(self):
        """
        通过创建人创建计划
        :return:
        """

    def search_by_keywords(self):
        """
        通过关键字搜索
        :return:
        """

    def openExResult(self):
        """
        查看计划详情
        :return:
        """
        sleep(3)
        self.find_element_by_text(planTaskName).click()
        # self.find_element_by_text().click()
        sleep(3)

    def generateDpTask(self):
        self.openExResult()
        sleep(3)
        # 点击生成点评任务
        self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[2]/div[2]/button[2]').click()
        sleep(3)
        # 点击确定
        self.find_element(By.XPATH,
                          "//span[@class='dialog-footer']/Button[@class='el-button el-button--primary']").click()