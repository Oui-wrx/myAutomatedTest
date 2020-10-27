# -*- coding: utf-8 -*-
# @Author : wrx
import allure
from selenium.webdriver.common.by import By

from public.page_obj.mzDpTaskPage import MzDpTaskPage
from public.page_obj.mzDpTaskTablePage import MzDpTaskTablePage


@allure.feature("点评阶段测试用例")
class Test_dp:

    @allure.story("全部批量点评，认同结果")
    def test_batchesDp(self, go_login):
        mzDpTaskpage = MzDpTaskPage(go_login)
        mzDpTaskpage.openDpTask(2)
        mzDpTaskTablePage = MzDpTaskTablePage(go_login)
        mzDpTaskTablePage.checkAll()
        mzDpTaskTablePage.IdentityResults()
        mzDpTaskTablePage.ok()

    @allure.story("提交审核测试")
    def test_subAudit(self, go_login):
        mzDpTaskpage = MzDpTaskPage(go_login)
        mzDpTaskpage.openDpTask(2)
        mzDpTaskTablePage = MzDpTaskTablePage(go_login)
        mzDpTaskTablePage.submitAudit()
        mzDpTaskTablePage.ok()


if __name__ == '__main__':
    pass
