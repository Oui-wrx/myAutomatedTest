import pytest

from public.page_obj.login import Login

username = "admin"
password = "123"


# @pytest.fixture(scope="package")
# def go_login():
#     """
#     定义登录
#     :return:
#     """
#     Login().login(username, password)

# 用于解决mark标记警告问题
# def pytest_configure(config):
#     marker_list = ["a", "b"]   # 标签名集合
#     for markers in marker_list:
#         config.addinivalue_line(
#             "markers", markers
#         )
