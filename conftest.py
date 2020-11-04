# -*- coding: utf-8 -*-
# @Author : wrx

# 定义全局打开浏览器
import pytest
from selenium import webdriver


# @pytest.fixture(scope="session", autouse=True)
# def my_driver():
#     """定义全局浏览器驱动"""
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
