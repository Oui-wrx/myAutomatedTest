# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage
from public.page_obj.firstPage import FirstPage

username = "admin"
password = "123"


class MzDpTaskPage(BasePage):
    """
    门诊点评列表页
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://172.16.0.166:8034/index.html#/Outpatient")
        sleep(2)

    def page_check(self):
        """
        页面检查
        :return:
        """

    def search_myWork(self):
        """
        筛选我的任务
        :return:
        """

    def search_by_workStatus(self):
        """
        根据任务状态筛选
        :return:
        """

    def search_by_dpPeople(self):
        """
        根据点评人筛选
        :return:
        """

    def search_by_shPeople(self):
        """
        根据审核人筛选
        :return:
        """

    def search_by_replyPeople(self):
        """
        根据回复反馈人筛选
        :return:
        """

    def search_by_keywords(self):
        """
        根据任务关键字筛选
        :return:
        """

    def openDpTask(self, id):
        """
        打开某个点评任务：
        :param id: 正序
        :return:
        """
        sleep(3)
        # //*[@id="app"]/div/section/main/div/div[4]/div/div[3]/table/tbody  //*[@id="app"]/div/section/main/div/div[4]/div/div[3]/table/tbody
        taskTbody = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[3]/div/div[3]/table/tbody')
        taskTrList = taskTbody.find_elements(By.TAG_NAME, "tr")
        taskTrList[id].click()
        sleep(4)

    def openMzDp(self):
        """
        点评
        :return:
        """

    def openMzSh(self):
        """
        审核
        :return:
        """

    def openMzReplyFeedback(self):
        """
        回复反馈
        :return:
        """
