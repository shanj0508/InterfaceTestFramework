# -*- coding: utf-8 -*-
import pytest

from pytest_interface.api_keyword.api_key import ApiKey


class Test_ApiCase():
    def test01(self):
        # 初始化工具类
        ak = ApiKey()
        # 定义接口url
        url = "http://172.16.6.240/eap/doLogin.action"
        # 定义请求参数
        userInfo = {
            "loginName": "admin",
            "loginPassword": "O8I1xE0y0yr42UAfZeZ9lBSABcLd0yFO8Foi6EW6dyFw3noQrte8i4kzrq3CC0GBAjINzFRaPettaAj5BdP02WQx4FATlVNFn42o2AM4Nsc0PDhZf+PpNvz+rld2cITo4zKgoU6EoV/k5voPECvpbQ9l6mfLYWL3WyYdVx1PDf0="
        }
        # 定义请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        r = ak.get(url=url, data=userInfo, headers=headers)
        print(r.text)
        # 获取响应结果，用于校验是否成功
        msg = ak.get_jsontext(r.text, 'msg')
        print(msg)
        assert msg == 'success'


if __name__ == '__main__':
    pytest.main(['-s', 'test_case01.py'])
