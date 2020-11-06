# # -*- coding: utf-8 -*-
# # @Author : wrx
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# from public.page_obj.main import FirstPage
#
#
# class FunctionSwitchPage(FirstPage):
#
#     def __init__(self, selenium_driver):
#         super().__init__(selenium_driver)
#         self.find_element_by_text("配置").click()
#
#     def open_notice(self):
#         ele = self.find_element("xpath", "//*[@id='app']/div/section/main/div/div[3]/div/div["
#                                          "1]/div/div/div/div/span")
#         ele_style = ele.get_attribute("style")
#         if ele_style == 'width: 40px; border-color: rgb(19, 206, 102); background-color: rgb(19, 206, 102);':
#             pass
#         else:
#             ele.click()
#         self.find_element("xpath", '//*[@id="app"]/div/section/main/div/div[3]/div/div[2]/div[2]/button/span').click()
#
#     def set_process(self, moduleName):
#         self.find_element("xpath",
#                           '//*[@id="app"]/div/section/main/div/div[3]/div/div[2]/div[1]/div[1]/div/div/input').click()
#         self.fin
