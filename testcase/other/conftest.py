import pytest

from public.page_obj.login import Login

username = "admin"
password = "123"


# # , autouse=True
# @pytest.fixture(scope="package")
# def go_login(my_driver):
#     """
#     定义登录
#     :return:
#     """
#     station = Login(my_driver).login(username, password)
#     # driver.implicitly_wait(10)
#     # driver.refresh()
#     yield station
