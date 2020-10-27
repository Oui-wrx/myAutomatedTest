# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

from selenium.webdriver.common.by import By

from public.page_obj.basePage import BasePage
from public.page_obj.resultPublicPage import ResultPublicPage


class DpDetailsPage(BasePage):
    """
    点评详情页
    """

    def __init__(self, driver):
        super().__init__(driver)

    def acceptOpinions(self, flag):
        """
        采纳意见
        :return:
        """
        self.find_element_by_text("采纳意见").click()
        if flag:  # 确定
            self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > '
                                               'button.el-button.el-button--primary').click()
            assert self.find_element_by_text("待归档"), "确认采纳意见失败"
        else:     # 取消
            self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > '
                                               'button.el-button.el-button--default').click()
            assert self.find_element_by_text("采纳意见"), "取消采纳意见失败"

    def continueFeedback(self):
        """
        继续反馈
        :return:
        """
        self.find_element_by_text("继续反馈").click()

    def dpReasonable(self):
        """
        点评合理
        :return:
        """
        self.find_element(By.XPATH, '//*[@id="pane-first"]/div/div/div[1]/label[1]/span[1]/span').click()
        self.find_element_by_text("保存复评").click()

    def dpUnReasonable(self):
        """
        点评不合理
        :return:
        """
        self.find_element(By.XPATH, '//*[@id="pane-first"]/div/div/div[1]/label[2]/span[1]/span').click()
        self.find_element_by_text("保存复评").click()

    def goFeedback(self, content):
        """
        我要反馈
        :return:
        """
        assert self.find_element_by_text("我要反馈"), "我要反馈  按钮没找到"
        self.find_element_by_text("我要反馈").click()
        sleep(2)
        assert self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.huifushenhe > div > '
                                                  'div.el-dialog__body > div:nth-child(2) > div > textarea')
        self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.huifushenhe > div > div.el-dialog__body > '
                                           'div:nth-child(2) > div > textarea').send_keys(content)

    def insistResult(self, useTemplate=None, remarks=None):
        """
        坚持原点评结果
        :param useTemplate: 是否使用模板
        :param remarks: 理由：必填项
        :return:
        """
        # assert self.find_element_by_text("请先填写坚持原点评结果的理由，再继续回复反馈的操作"), "必须填写理由"
        if useTemplate:  # 不使用模板  应该提示输入
            self.find_element(By.XPATH, "//input[@placeholder='回复反馈理由模板']").click()
        # 暂时使用文本定位
        self.find_element_by_text("回复反馈11").click()
        self.submit()
        # 回复确认
        # self.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/span/button[2]').click()
        self.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div.el-dialog__footer > span > "
                                           "button.el-button.el-button--primary").click()

    def modifyResult(self, modifyStatus, remarks, useTemplate=None):
        """
        修改原点评结果
        :param modifyStatus: 点评结果修改状态 0 标识未修改  1 标识修改了
        :param remarks: 理由
        :param useTemplate: 是否使用模板
        :return:
        """
        if modifyStatus:
            if useTemplate is None:
                self.find_element(By.CSS_SELECTOR, 'body > div:nth-child(11) > div > div.el-dialog__body > '
                                                   'div:nth-child(3) > div > textarea').send_keys(remarks)
            # 需要加个理由
            self.submit()

    def ok(self):
        """
        点击确定
        :return:
        """
        # body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary
        assert self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.huifushenhe > div > '
                                                  'div.el-dialog__footer > span > '
                                                  'button.el-button.el-button--primary'), "元素没找到"
        self.find_element(By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.huifushenhe > div > div.el-dialog__footer > '
                                           'span > button.el-button.el-button--primary').click()
        sleep(2)

    def replyFeedback(self, do, useTemplate=None, remarks=None):
        """
        回复反馈
        :param do: 坚持原点评结果 or  修改点评结果
        :param useTemplate: 是否使用模板
        :param remarks: 理由
        :return:
        """
        assert self.find_element_by_text("回复反馈"), "回复反馈  按钮没找到"
        self.find_element_by_text("回复反馈").click()
        sleep(2)
        if do == "坚持原点评结果":
            self.insistResult(useTemplate, remarks)
        else:
            # self.modifyResult()
            pass

    def submit(self):
        """
        点击提交
        :return:
        """
        # /html/body/div[8]/div/div[3]/span/button[2]/span  回复反馈得提交
        # self.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/span/button[2]/span").click()  // 我要反馈的提交
        self.find_element(By.XPATH, "//div/div[3]/span/button[2]/span").click()  # 尝试我要反馈的提交
        sleep(2)
        # 回复反馈，提交，在提交  /html/body/div[6]/div/div[3]/span/button[2]  不可用该方法

    def goResultPublicPage(self):
        """
        前往结果公示页面
        :return:
        """
        ResultPublicPage(self.driver)
