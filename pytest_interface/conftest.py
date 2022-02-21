# -*- coding: utf-8 -*-
from class0221_apiTest.pytest_interface.api_keyword.api_key import ApiKey
from class0221_apiTest.pytest_interface.params.allParams import *


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 项目级fix:整个项目只初始化一次
@pytest.fixture(scope='session')
def token_fix():
    # 初始化工具类
    ak = ApiKey()
    with allure.step("发送登录接口请求，生成token值，整个项目仅生成一次"):
        # 定义url
        # url = "http://172.16.6.240/eap/doLogin.action"
        url = URL + PORT + "/eap/doLogin.action"
        # 定义请求参数
        data = {
            "loginName": "admin",
            "loginPassword": "O8I1xE0y0yr42UAfZeZ9lBSABcLd0yFO8Foi6EW6dyFw3noQrte8i4kzrq3CC0GBAjINzFRaPettaAj5BdP02WQx4FATlVNFn42o2AM4Nsc0PDhZf+PpNvz+rld2cITo4zKgoU6EoV/k5voPECvpbQ9l6mfLYWL3WyYdVx1PDf0="
        }
        # 定义请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        # 发送post请求
        res = ak.post(url=url, data=data, headers=headers)
        # 获取token
        token = ak.get_jsontext(res.text, 'tokenId')
        print("tokenID:", token)
        return ak, token, res
