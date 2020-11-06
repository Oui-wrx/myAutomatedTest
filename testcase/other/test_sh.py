# # -*- coding: utf-8 -*-
# # @Author : wrx
# import allure
# from selenium.webdriver.common.by import By
#
# from public.page_obj.mzDpTaskPage import MzDpTaskPage
# from public.page_obj.mzDpTaskTablePage import MzDpTaskTablePage
#
#
# @allure.feature("审核阶段测试用例")
# class Test_sh:
#
#     @allure.story("全部批量审核，认同结果")
#     def test_batchesSh(self, go_login):
#         mzDpTaskpage = MzDpTaskPage(go_login)
#         mzDpTaskpage.openDpTask(2)
#         mzDpTaskTablePage = MzDpTaskTablePage(go_login)
#         mzDpTaskTablePage.checkAll()
#         mzDpTaskTablePage.auditPass()
#         mzDpTaskTablePage.ok()
#
#     @allure.story("生成点评工作表")
#     def test_create(self, go_login):
#         mzDpTaskpage = MzDpTaskPage(go_login)
#         mzDpTaskpage.openDpTask(2)
#         mzDpTaskTablePage = MzDpTaskTablePage(go_login)
#         mzDpTaskTablePage.generateWorkTable()
#         mzDpTaskTablePage.ok()
#
#
# if __name__ == '__main__':
#     pass
