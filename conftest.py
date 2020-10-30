# -*- coding: utf-8 -*-
# @Author : wrx

# 定义全局打开浏览器
import pytest
from selenium import webdriver

url = "http://172.16.0.166:8034/index.html"


@pytest.fixture(scope="session", autouse= True)
def driver():
    """定义全局浏览器驱动，并打开登录页面"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
