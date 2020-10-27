# -*- coding: utf-8 -*-
# @Author : wrx
import pytest

username = "admin"
password = "123"

test_user_data = ["管理员", "其他角色"]


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入的参数
    user = request.param
    print(user)
    return user


# indirect=True，可以把传递过来的参数当做函数执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login11(login_r):
    a = login_r
    assert a != ""
