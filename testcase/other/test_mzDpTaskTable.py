# -*- coding: utf-8 -*-
# @Author : wrx
import allure
import pytest

from public.models.myunit import MyUnit
from public.page_obj.mzDpTaskTablePage import MzDpTaskTablePage


@allure.feature("点评任务表")
class Test_mzDpTaskTable(MyUnit):

    @allure.story("批量点评，提交审核")
    # @pytest.mark.dependency(name="openDpTaskTable", depends=["generateDpWork"], scope="package")
    def test_batch_dp(self):
        mzDpTaskTablePage = MzDpTaskTablePage(self.driver)
        mzDpTaskTablePage.operate_dpTask()

    @allure.story("批量审核")
    def test_batch_sh(self):
        mzDpTaskTablePage = MzDpTaskTablePage(self.driver)
        mzDpTaskTablePage.operate_shTask()

    @allure.story("生成点评工作表")
    def test_generateDpWorkTable(self):
        mzDpTaskTablePage = MzDpTaskTablePage(self.driver)
        mzDpTaskTablePage.generate_dpWorkTable()

    @allure.story("发送点评工作表")
    def test_sendDpWorkTable(self):
        mzDpTaskTablePage = MzDpTaskTablePage(self.driver)
        mzDpTaskTablePage.send_dpWorkTable()

    @allure.story("回复反馈")
    def test_replyFeedback(self):
        mzDpTaskTablePage = MzDpTaskTablePage(self.driver)
        mzDpTaskTablePage.reply_feedback(1)


if __name__ == '__main':
    pytest.main("测试用例", "-s")
