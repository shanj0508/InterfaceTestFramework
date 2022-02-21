# -*- coding: utf-8 -*-
import pytest

from class0221_apiTest.pytest_interface.api_keyword.api_key import ApiKey
from class0221_apiTest.pytest_interface.data_driver import yaml_driver
from class0221_apiTest.pytest_interface.params.allParams import *


@allure.epic("接口测试")
class Test_ApiCase()
    # 参数化
    @allure.story("01.登录接口测试")
    @pytest.mark.paramtrize('userData', yaml_driver.load_yaml('./data/user.yaml'), ids=[
        "输入正确账号密码，登陆成功",
        "输入错误账号密码，登陆失败",
        "输入错误账号密码，登陆失败"
    ])
    def test01_doLogin(self, userData):
        # 初始化工具类
        ak = ApiKey()
        # 定义接口url
        # url = "http://172.16.6.240/eap/doLogin.action"
        url = URL + PORT + "/eap/doLogin.action"
        # 定义请求参数
        userInfo = {
            "loginName": userData['user']['username'],
            "loginPassword": userData['user']['password']
        }
        # 定义请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        r = ak.get(url=url, data=userInfo, headers=headers)
        print(r.text)
        # 获取响应结果，用于校验是否成功
        with allure.step("校验响应结果"):
            msg = ak.get_jsontext(r.text, 'msg')
            print(msg)
            assert msg == userData['msg']

    @allure.story("02.查询用户列表接口测试")
    def test02_getUserInfo(self, token_fix):
        # 从fix中获取预置的工具类
        # 所有返回都要获取
        ak, token, res = token_fix
        with allure.step("发送查询用户列表接口请求"):
            # url = "http://172.16.6.240/eap/eobs/user/userData.action"
            url = URL + PORT + "/eap/eobs/user/userData.action"
            data = {
                "limit": 20,
                "start": 0
            }
            # 定义请求头
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'tokenId': token
            }
            r1 = ak.get(url=url, data=data, headers=headers)
            print(r1.text)

        with allure.step("校验响应结果"):
            msg = ak.get_jsontext(r1.text, 'msg')
            print(msg)
            assert msg == 'success'
        return r1

    @allure.story("03.查询用户列表接口测试2")
    def test03_getUserInfo_1(self, token_fix):
        # 从fix中获取预置的工具类
        # 所有返回都要获取
        ak, token, res = token_fix
        with allure.step("调用test02_getUserInfo接口，获取响应值"):
            r1 = self.test02_getUserInfo(token_fix)  # 可以在请求中直接使用上个接口的响应r1

        with allure.step("发送查询用户列表接口请求"):
            # url = "http://172.16.6.240/eap/eobs/user/userData.action"
            url = URL + PORT + "/eap/eobs/user/userData.action"
            data = {
                "limit": 20,
                "start": 0
            }
            # 定义请求头
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'tokenId': token
            }
            r1 = ak.get(url=url, data=data, headers=headers)
            print(r1.text)

        with allure.step("校验响应结果"):
            msg = ak.get_jsontext(r1.text, 'msg')
            print(msg)
            assert msg == 'success'


if __name__ == '__main__':
    pytest.main(['-s', 'test_case04.py'])
