# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage


class MzDpTaskTablePage(BasePage):
    """
    门诊点评任务表
    """

    def __init__(self, driver):
        super().__init__(driver)

    def viewDetails(self):
        """
        查看计划详情
        :return:
        """
        self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[1]/div[1]/div[1]/div/i').click()

    def submitAudit(self):
        """
        点击提交审核
        :return:
        """
        assert self.find_element_by_text("提交审核"), '元素没找到'
        self.find_element_by_text("提交审核").click()

    def autoReview(self):
        """
        重新自动点评
        :return:
        """
        self.find_element(By.XPATH,
                          "//*[@id='app']/div/section/main/div/div[1]/div[1]/div[2]/div[2]/div/span/span[contains(text(), '更多')]").click()
        self.find_element_by_text("重新自动点评").click()

    def setPreparation(self, whoWork=None, statusWork=None, personDp=None, autoDp=None, more=None):
        """
        设置筛选项
        :param whoWork: 我的任务
        :param statusWork: 任务状态
        :param personDp: 人工点评
        :param autoDp: 自动点评
        :param more: 更多筛选条件
        :return:
        """
        if whoWork:
            self.find_element(By.XPATH, "//input[@placeholder='全部任务']").click()
            self.find_element_by_text(whoWork).click()
        if statusWork:
            self.find_element(By.XPATH, "//input[@placeholder='全部状态']").click()
            statusWork = "[contains(text(), '" + statusWork + "')]"
            self.find_element(By.XPATH, "//div/div/div/ul/li/span" + statusWork).click()
        if personDp:
            self.find_element(By.XPATH, "//input[@placeholder='人工点评']").click()
            personDp = "[contains(text(), '" + personDp + "')]"
            self.find_element(By.XPATH, "//div/div/div/ul/li/span" + personDp).click()
        if autoDp:
            self.find_element(By.XPATH, "//input[@placeholder='自动点评']").click()
            autoDp = "[contains(text(), '" + autoDp + "')]"
            self.find_element(By.XPATH, "//div/div/div/ul/li/span" + autoDp).click()

    def setMorePreparation(self):
        """
        设置更多筛选条件
        :return:
        """
        self.find_element_by_text("更多").click()  # 有问题
        # 不会写了

    def openPrescription(self, id):
        """
        根据Id 打开某条处方或医嘱
        :param id:
        :return:
        """
        taskTbody = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[2]/div/div[4]/table/tbody')
        taskTrList = taskTbody.find_elements(By.TAG_NAME, "tr")
        taskTrList[id].click()
        sleep(4)

    def preparation(self):
        """
        点击筛选按钮
        :return:
        """
        element = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[1]/div[4]/div[1]/div['
                                              '1]/button[1]/span')
        assert element
        element.click()

    def reset(self):
        """
        点击重置按钮
        :return:
        """
        element = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[1]/div[4]/div[1]/div['
                                              '1]/button[2]/span')
        assert element
        element.click()

    def checkAll(self):
        """
        任务表点击全选
        :return:
        """
        self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[2]/div/div[5]/div[1]/table/thead/tr/th['
                                    '1]/div/label/span/span').click()

    def checkSome(self, *some):
        """
        选中某几行
        :param some:被选中行的序号
        :return:
        """
        taskTbody = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[2]/div/div[5]/div['
                                                '3]/table/tbody')
        assert taskTbody
        taskTrList = taskTbody.find_elements(By.TAG_NAME, "tr")
        assert taskTrList
        for s in some:
            ele = taskTrList[s].find_element(By.XPATH, '//td[1]/div/label/span/span')
            ActionChains(self.driver).move_to_element(taskTrList[s]).perform()
            ActionChains(self.driver).move_to_element(ele).click().perform()
            # ele.click()
            sleep(2)

    def confirmReasonable(self):
        """
        确认合理
        :return:
        """
        assert self.find_element_by_text("确认合理").click()

    def IdentityResults(self):
        """
        认同结果
        :return:
        """
        self.find_element_by_text("认同结果").click()

    def remove(self):
        """
        确定合理/认同结果后，点击取消
        :return:
        """
        assert self.find_element(By.XPATH, "//div/div[3]/button[1]/span").click()

    def ok(self):
        """
        点击确定
        :return:
        """
        # 点评审核阶段的确定好用
        if self.find_element(By.CSS_SELECTOR, "body > div.w-message-box__wrapper > div > div.w-message-box__btns "
                                              ">button.w-button.w-button--default.w-button--small.w-button--primary >"
                                              " span"):
            self.find_element(By.CSS_SELECTOR, "body > div.w-message-box__wrapper > div > div.w-message-box__btns > "
                                               "button.w-button.w-button--default.w-button--small.w-button--primary > "
                                               "span").click()
        else:  # 发送点评工作表的确定好用
            self.find_element(By.CSS_SELECTOR, "#app > div > section > main > div > div:nth-child(1) > div.nav > "
                                               "div.Submission > div:nth-child(4) > div:nth-child(2) > div > "
                                               "div.el-dialog__footer > span > button.el-button.el-button--primary > "
                                               "span").click()

    def auditPass(self):
        """
        审核通过
        :return:
        """
        assert self.find_element_by_text("审核通过"), '审核通过 按钮元素没找到'
        self.find_element_by_text("审核通过").click()

    def generateWorkTable(self):
        """
        生成工作表
        :return:
        """
        assert self.find_element_by_text("生成工作表"), '生成工作表 按钮元素没找到'
        self.find_element_by_text("生成工作表").click()
        sleep(2)

    def sendWorkTable(self):
        """
        发送工作表
        :return:
        """
        assert self.find_element_by_text("发送工作表"), '发送工作表 按钮元素没找到'
        self.find_element_by_text("发送工作表").click()
        sleep(2)

    # def reply_feedback(self, status):
    #     sleep(4)
    #     self.find_element_by_text("15:25:47").click()
    #     sleep(5)
    #     # 查找反馈待处理  tr[2]   可以以行 为目标
    #     self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[2]/div/div[4]/table/tbody/tr[2]").click()
    #     sleep(3)
    #     # 点击回复反馈
    #     self.find_element(By.XPATH, "//*[@id='app']/div/section/main/div/div[4]/div/div/div/div[2]/div/div[2]/div["
    #                                 "4]/div/div[1]/span/button").click()
    #     if status:
    #         # 1 ：坚持原点评结果
    #         # 点击理由
    #         self.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > "
    #                                            "div:nth-child(3) > span > div > div > span > span > i").click()
    #         # 选择模板
    #         self.find_element_by_text("回复反馈11").click()
    #         # 点击提交
    #         self.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > "
    #                                            "button:nth-child(2) > span").click()
    #         sleep(3)
    #         #  确认回复
    #         self.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/span/button[2]").click()
    #         sleep(5)
    #     else:
    #         # 0 : 修改点评结果
    #         self.find_element_by_text("修改点评结果").click()
    #         # 点击提交
    #         self.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > "
    #                                            "button:nth-child(2) > span").click()
    #         sleep(5)
