# -*- coding: utf-8 -*-
# @Author : wrx
import allure
import ddt
import pytest

from public.page_obj.exResultsPage import ExResultsPage


@allure.feature("抽取结果列表页")
class Test_exResult:
    # @allure.story("打开抽取结果详情")
    # def test_openExResultDetails(self):
    #     exResult = ExResultsPage(self.driver)
    #     exResult.openExResult()

    @allure.story("生成点评任务")
    @pytest.mark.dependency(name="generateDpWork", depends=["exPlan"], scope="package")
    def test_generateDpWork(self, go_login):
        driver = go_login
        exResult = ExResultsPage(driver)
        exResult.generateDpTask()


if __name__ == "__main__":
    pytest.main(["test_dpjh.py", "test_exResult.py"], "-s")
