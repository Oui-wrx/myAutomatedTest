# # -*- coding: utf-8 -*-
# # @Author : wrx
# from time import sleep
#
# from selenium.webdriver.common.by import By
#
# from public.page_obj.basePage import BasePage
#
#
# class PublicDpWorkTable(BasePage):
#     """
#     点评工作表-公示
#     """
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         sleep(2)
#
#     def page_check(self):
#         """
#         页面检查
#         :return:
#         """
#
#     def openPrescription(self, id):
#         """
#         打开单条点评任务（处方、医嘱）
#         :param id: 从0开始   正序
#         :return:
#         """
#         taskTbody = self.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div/div[4]/table/tbody')
#         taskTrList = taskTbody.find_elements(By.TAG_NAME, "tr")
#         taskTrList[id].click()
#         sleep(3)
