# -*- coding: utf-8 -*-
# @Author : wrx
from public.page_obj.basePage import BasePage


class AddOrEditZyPlanPage(BasePage):
    """
    新增住院计划页
    """

    # 计划名称
    planNameLoc = ("xpath", '//*[@id="app"]/div/section/main/div/div[1]/div[2]/div[1]/div/input')
    # 计划描述
    planDescriptionLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[1]/div[2]/div[2]/div/textarea')

    # 随机抽取（）份
    randomExFenLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/input')
    # 随机抽取（）%
    randomExtractPerLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/input')
    # 科室or病区1
    departmentOrBqOneLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/input')
    # 科室1
    departmentOneLoc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    # 病区1
    bqOneLoc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    # 每个 科室/病区 （）份
    perDepOrBqFenLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[2]/input')
    # 科室or病区2
    departmentOrBqTwoLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[3]/div/input')
    # 科室2
    departmentTwoLoc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    # 病区2
    bqTwoLoc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    # 每个 科室/病区 （）%
    perDepOrBqPerLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[4]/input')
    # 随机抽取（）主管医生
    numExByDocLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div[1]/input')
    # 随机抽取 % / 位 医生
    unitExByDocLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div[2]/div/input')
    # 位 医生
    weiExByDocLoc = ('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[2]/span')
    # % 医生
    perExByDocLoc = ('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    # 随机抽取开嘱/主管医生
    typeDocLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div[3]/div/input')
    # 随机抽取开嘱医生
    kaiZhuDocLoc = ('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]/span')
    # 随机抽取主管医生
    zhuGuanDocLoc = ('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[2]/span')
    # 每位医生抽取下限
    docExDownLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div[4]/input')
    # 每位医生抽取上限
    docExUpLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div[5]/input')
    # 等间隔抽取
    perSpaceExLoc = ('xpath', '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div[2]/div[4]/div/input')

    #
