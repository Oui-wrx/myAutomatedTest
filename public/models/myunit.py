# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 17:08
# @Author  : wrx
import unittest
from .driver import WDriver


class MyUnit(unittest.TestCase):
    """
    自定义MyUnit
    """

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = WDriver().chromeDriver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
