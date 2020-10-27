import pytest
from selenium import webdriver

from public.page_obj.loginPage import LoginPage

global driver

username = "admin"
password = "123"


@pytest.fixture(scope="package")
def go_login(open_brower):
    """
    定义登录
    :param open_brower:
    :return:
    """
    driver = open_brower
    LoginPage(driver).login(username, password)
    driver.refresh()
    yield driver
    driver.quit()


# 用于解决mark标记警告问题
def pytest_configure(config):
    marker_list = ["a", "b"]   # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
