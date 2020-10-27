# -*- coding: utf-8 -*-
# @Author : wrx

# 定义全局打开浏览器
import pytest
from selenium import webdriver

url = "http://172.16.0.166:8034/index.html"


@pytest.fixture(scope="session")
def open_brower():
    """定义全局浏览器驱动"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()