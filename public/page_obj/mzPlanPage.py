# -*- coding: utf-8 -*-
# @Author : wrx

from selenium.webdriver.common.by import By

from public.models.read_yaml_data import read_yamlData
from public.page_obj.basePage import BasePage
from public.page_obj.moreConditionPage import MoreConditionsPage

webElement = read_yamlData(r"\public\webElement\addPlan.yaml")


class MzPlanPage(BasePage):
    """
    新增计划页面
    """

    def inputPlanName(self, name):
        """
        输入计划名称
        :param name:
        :return:
        """
        self.find(webElement["计划名称"]).send_keys(name)

    def inputPlanDescription(self, description):
        """
        输入计划描述
        :param description:
        :return:
        """
        self.find(webElement["计划描述"]).send_keys(description)

    def inputExByDep(self, num, unit):
        """
        按照科室抽取
        :param num:
        :param unit:
        :return:
        """
        if unit is '份':
            self.find(webElement["每个科室份数"]).send_keys(num)
        if unit is "%":
            self.find(webElement["每个科室%"]).send_keys(num)

    def inputExPerSpace(self, num):
        """
        等间隔抽取
        :param num:
        :return:
        """
        self.find(webElement["等间隔抽取份"]).send_keys(num)

    def inputExRandom(self, num, unit, down=None, up=None):
        """
        设置随机抽取
        :param up: 数量上限
        :param down: 数量下限
        :param num: 抽取数（份数 / %）
        :param unit: 抽取医生的单位
        :return: 设置好的随机抽取条件
        """
        if unit is '份' and down is None and up is None:
            self.find(webElement["随机抽取份数"]).send_keys(num)  # 随机抽取（）份
        elif unit is "%" and down is None and up is None:
            self.find(webElement["随机抽取%"]).send_keys(num)  # 随机抽取（）%
        else:
            self.find(webElement["随机抽取处方医生数"]).send_keys(num)  # 随机（）医生
            if unit is '位':
                self.find(webElement["随机抽取处方医生单位"]).click()
                self.find(webElement["随机抽取处方医生位"]).click()  # 设置（）位医生  默认为%
            self.find(webElement["随机抽取处方医生下限"]).send_keys(down)
            self.find(webElement["随机抽取处方医生上限"]).send_keys(up)  # 设置 抽取的上下限

    def inputPlanFrequency(self, unit, day=None, exTime=None):
        """
        设置计划频次
        :param unit: 季度  月   单次
        :param day:  数量  单次计划时  为None
        :param exTime: 处方时间or就诊时间
        :return:
        """
        if unit is "每月定期计划":
            self.find(webElement["每月定期抽取日"]).send_keys(day)
        elif unit is "每季度定期计划":
            self.find(webElement["每季度定期抽取日"]).send_keys(day)
        else:
            if exTime is "就诊时间":
                self.find(webElement["就诊时间类型"]).click()
                self.find(webElement["就诊时间"]).click()

    def cancellPlan(self):
        """
        取消保存计划
        :return:
        """
        self.find(webElement["取消"]).click()

    def savePlan(self):
        """
        保存计划
        :return:
        """
        self.find(webElement["保存"]).click()

    def extractPlan(self):
        """
        抽取计划
        :return:
        """
        self.find(webElement["抽取"]).click()

    def go_more_conditions(self):
        self.find(webElement["更多抽取条件"]).click()
        return MoreConditionsPage(self._driver)