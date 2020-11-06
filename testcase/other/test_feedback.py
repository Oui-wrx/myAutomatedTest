# # -*- coding: utf-8 -*-
# # @Author : wrx
# import allure
#
# from public.page_obj.dpDetailsPage import DpDetailsPage
# from public.page_obj.mzDpTaskPage import MzDpTaskPage
# from public.page_obj.mzDpTaskTablePage import MzDpTaskTablePage
# from public.page_obj.publicDpWorkTable import PublicDpWorkTable
# from public.page_obj.resultPublicPage import ResultPublicPage
#
#
# @allure.feature("反馈阶段测试用例")
# class Test_feedback:
#
#     @allure.story("单条反馈测试")
#     def test_goFeedback(self, go_login):
#         resultPublicPage = ResultPublicPage(go_login)
#         resultPublicPage.openDpWorkTable(0)
#         resultPublicPage.publicDpWorkTable().openPrescription(4)
#         dpDetailsPage = DpDetailsPage(go_login)
#         dpDetailsPage.goFeedback("意思一下，反馈一下")
#         dpDetailsPage.ok()
#         dpDetailsPage.submit()
#
#     @allure.story("回复反馈测试")
#     def test_replyFeedback(self, go_login):
#         mzDpTaskpage = MzDpTaskPage(go_login)
#         mzDpTaskpage.openDpTask(2)
#         mzDpTaskTablePage = MzDpTaskTablePage(go_login)
#         mzDpTaskTablePage.openPrescription(4)
#         dpDetailsPage = DpDetailsPage(go_login)
#         dpDetailsPage.replyFeedback("坚持原点评结果", 1)
#
#     @allure.story("采纳意见测试")
#     def test_acceptOpinions(self, go_login):
#         resultPublicPage = ResultPublicPage(go_login)
#         resultPublicPage.openDpWorkTable(0)
#         publicDpWorkTable = PublicDpWorkTable(go_login)
#         publicDpWorkTable.openPrescription(4)
#         dpDetailsPage = DpDetailsPage(go_login)
#         dpDetailsPage.acceptOpinions(True)
#
#
# if __name__ == '__main__':
#     pass
