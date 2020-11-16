# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 17:08
# @Author  : wrx
import unittest
from ..page_obj.main import Main


class MyUnit:
    """
    自定义MyUnit
    """

    def setup_class(self):
        self.main = Main()

    def teardown_class(self):
        self.main.get_driver().quit()
