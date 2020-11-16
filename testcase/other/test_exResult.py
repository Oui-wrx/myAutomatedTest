# -*- coding: utf-8 -*-
# @Author : wrx
from time import sleep

import allure
import pytest

from public.models.myunit import MyUnit
from public.page_obj.exResultsPage import ExResultsPage


@allure.feature("抽取结果列表页")
class Test_exResult(MyUnit):

    def setup(self):
        self.exResult = ExResultsPage(self.main.get_driver())
        self.exResult.at_page()

    def test(self):
        sleep(4)
        pass


if __name__ == "__main__":
    pytest.main(["test_dpjh.py", "test_exResult.py"], "-s")
