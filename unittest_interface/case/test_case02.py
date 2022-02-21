# -*- coding: utf-8 -*-
import unittest
from ddt import ddt, file_data

from class0221_apiTest.unittest_interface.api_keyword.api_key import ApiKey


@ddt
class Test_ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化工具类
        cls.ak = ApiKey()

    # 参数化
    @file_data('./data/user.yaml')
    def test01(self, user, msg):
        # 定义接口url
        url = "http://172.16.6.240/eap/doLogin.action"
        # 定义请求参数
        userInfo = {
            "loginName": user['username'],
            "loginPassword": user['password']
        }
        # 定义请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        r = self.ak.get(url=url, data=userInfo, headers=headers)
        print(r.text)
        # 获取响应结果，用于校验是否成功
        msg = self.ak.get_jsontext(r.text, 'msg')
        print(msg)
        self.assertEqual(msg, msg, msg='断言失败')


if __name__ == '__main__':
    unittest.main()
