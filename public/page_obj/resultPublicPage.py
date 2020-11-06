# # -*- coding: utf-8 -*-
# # @Author : wrx
# from time import sleep
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# from public.page_obj.basePage import BasePage
# from public.page_obj.publicDpWorkTable import PublicDpWorkTable
#
#
# class ResultPublicPage(BasePage):
#     """
#     结果公示页
#     """
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get("http://172.16.0.166:8034/index.html#/PublicityResult")
#         sleep(2)
#
#     def page_check(self):
#         """
#         页面检查
#         :return:
#         """
#
#     def openDpWorkTable(self, id):
#         """
#         打开点评工作表
#         :param id: 正序
#         :return:
#         """
#         taskTbody = self.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div[4]/div/div[3]/table/tbody')
#         taskTrList = taskTbody.find_elements(By.TAG_NAME, "tr")
#         taskTrList[id].click()
#         sleep(4)
#
#     def publicDpWorkTable(self):
#         return PublicDpWorkTable(self.driver)