# -*- coding: utf-8 -*-
import pytest

from pytest_interface.api_keyword.api_key import ApiKey
from pytest_interface.data_driver import yaml_driver


class Test_ApiCase():
    # 参数化
    @pytest.mark.paramtrize('userData', yaml_driver.load_yaml('../data/user.yaml'))
    def test01(self, userData):
        # 初始化工具类
        ak = ApiKey()
        # 定义接口url
        url = "http://172.16.6.240/eap/doLogin.action"
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
        msg = ak.get_jsontext(r.text, 'msg')
        print(msg)
        assert msg == userData['msg']


if __name__ == '__main__':
    pytest.main(['-s', 'test_case02.py'])
