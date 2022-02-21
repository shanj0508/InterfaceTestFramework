# -*- coding: utf-8 -*-

'''
    接口关键字驱动类：用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数内容即可。
    接口中常用的关键字：
        1.各种模拟请求方法：get/post/put/delete/header/……
        2.设置入参的默认值时，默认值参数必须放在最后

'''
import json

import allure
import requests


class ApiKey:
    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    @allure.step("发送post请求")
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)

    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    @allure.step("获取返回结果json字典值")
    def get_jsontext(self, data, key):
        # jsonpath获取数据的表达式：成功返回list,失败返回false
        # jsonpath接收的是dict类型的数据
        json_data = json.loads(data)
        value = jsonpath.jsonpath(json_data, '$..{0}'.format(key))
        return value[0]


if __name__ == '__main__':
    ak = ApiKey()
    # get请求
    # r = ak.get(url='http://172.16.6.240/eap/', timeout=1)
    # print(r.text)
    # post请求
    data = {
        "loginName": "admin",
        "loginPassword": "O8I1xE0y0yr42UAfZeZ9lBSABcLd0yFO8Foi6EW6dyFw3noQrte8i4kzrq3CC0GBAjINzFRaPettaAj5BdP02WQx4FATlVNFn42o2AM4Nsc0PDhZf+PpNvz+rld2cITo4zKgoU6EoV/k5voPECvpbQ9l6mfLYWL3WyYdVx1PDf0="
    }
    # 定义请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r = ak.post(url='http://172.16.6.240/eap/doLogin.action', data=data, headers=headers)
    print(r.text)
