# -*- coding: utf-8 -*-
# @Author : wrx
from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage


class AddOrEditMzPlanPage(BasePage):
    """
    新增门诊计划页面
    """
    # 计划概括元素
    mzPlanNameLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[1]/div/div[1]/div/input")
    mzPlanDesLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[1]/div/div[2]/div/textarea")
    # 抽取方式元素
    randomFenLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input")
    randomPerLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/input")
    exByDepFenLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input")
    exByDepPerLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input")
    exPerSpaceLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/input")
    randomNumByDocLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/input")
    randomUnitByDocLoc = ("xpath", "//*[@id='app']/div/section/main/div/div[2]/div/div[2]/div[2]/div[3]/div[3]/input")
    randomPerByDocLoc = ("xpath", '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    randomWeiByDocLoc = ("xpath", '/html/body/div[5]/div[1]/div[1]/ul/li[2]/span')
    randomDownByDocLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/div[2]/div[3]/div[4]/input')
    randomUpByDocLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/div[2]/div[3]/div[5]/input')
    # 计划频次元素
    dayPerMonthLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/div[1]/div/input')
    dayPerQuarterLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div/input')
    timeTypeLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/div[3]/div[1]/div/input')
    jiuZhenTimeLoc = ('xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]/span')
    # 取消、保存、抽取按钮
    cancellLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[5]/button[1]')
    saveLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[5]/button[2]')
    extractLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[5]/button[3]')

    def inputPlanName(self, name):
        """
        输入计划名称
        :param name:
        :return:
        """
        self.find_element(*self.mzPlanNameLoc).send_keys(name)

    def inputPlanDescription(self, description):
        """
        输入计划描述
        :param description:
        :return:
        """
        self.find_element(*self.mzPlanDesLoc).send_keys(description)

    def inputExByDep(self, num, unit):
        """
        按照科室抽取
        :param num:
        :param unit:
        :return:
        """
        if unit is '份':
            self.find_element(*self.exByDepFenLoc).send_keys(num)
        if unit is "%":
            self.find_element(*self.exByDepPerLoc).send_keys(num)

    def inputExPerSpace(self, num):
        """
        等间隔抽取
        :param num:
        :return:
        """
        self.find_element(*self.exPerSpaceLoc).send_keys(num)

    def inputExRandom(self, num, unit, down=None, up=None):
        """
        随机抽取
        :param up:
        :param down:
        :param num:
        :param unit:
        :return:
        """
        if unit is '份' and down is None and up is None:
            self.find_element(*self.randomFenLoc).send_keys(num)  # 随机抽取（）份
        elif unit is "%" and down is None and up is None:
            self.find_element(*self.randomPerLoc).send_keys(num)  # 随机抽取（）%
        else:
            self.find_element(*self.randomNumByDocLoc).send_keys(num)  # 随机（）医生
            if unit is '位':
                self.find_element(*self.randomUnitByDocLoc).click()
                self.find_element(*self.randomWeiByDocLoc).click()  # 设置（）位医生  默认为%
            self.find_element(*self.randomDownByDocLoc).send_keys(down)
            self.find_element(*self.randomUpByDocLoc).send_keys(up)  # 设置 抽取的上下限

    def inputPlanFrequency(self, unit, day=None, exTime=None, begin=None, end=None):
        """
        设置计划频次
        :param unit: 季度  月   单次
        :param day:  数量  单次计划时  为None
        :param exTime: 处方时间or就诊时间
        :param begin: 单次计划的开始日期
        :param end:  单次计划的结束日期
        :return:
        """
        if unit is "每月定期计划":
            self.find_element(*self.dayPerMonthLoc).send_keys(day)
        elif unit is "每季度定期计划":
            self.find_element(*self.dayPerQuarterLoc).send_keys(day)
        else:
            if exTime is "就诊时间":
                self.find_element(*self.timeTypeLoc).click()
                self.find_element_by_text("就诊时间").click()
            self.set_calendar(*begin)
            self.set_calendar(*end)

    def cancellPlan(self):
        """
        取消保存计划
        :return:
        """
        self.find_element(*self.cancellLoc).click()

    def savePlan(self):
        """
        保存计划
        :return:
        """
        self.find_element(*self.saveLoc).click()

    def extractPlan(self):
        """
        抽取计划
        :return:
        """
        self.find_element(*self.extractLoc).click()