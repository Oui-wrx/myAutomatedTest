import pytest

from public.page_obj.loginPage import LoginPage

username = "admin"
password = "123"


@pytest.fixture(scope="package", autouse=True)
def driver(driver):
    """
    定义登录
    :return:
    """
    LoginPage(driver).login(username, password)
    driver.implicitly_wait(10)
    driver.refresh()
    yield driver
