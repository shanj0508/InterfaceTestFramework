# -*- coding: utf-8 -*-

'''
    JsonPath模块：是专门用于处理Json字符串的模块,JsonPath相当于ui自动化中的Xpath
    部署JsonPath：通过pip install jsonpath 来进行安装
    通过JsonPath获得的内容，会以list的形式返回，也就意味着返回结果可以是一个值或者多个值同时存在的。

'''
import jsonpath, json

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

# 基于JsonPath获取元素：通过JsonPath函数来获取（json数据、定位表达式）
bike = jsonpath.jsonpath(data, '$.store.bicycle.color')
print(bike)  # ['red']
print(bike[0])  # red

book = jsonpath.jsonpath(data, '$.store.book[0].title')
print(book)

price = jsonpath.jsonpath(data, '$.store..price')
print(price)

book_price = jsonpath.jsonpath(data, '$.store.book[0,1].price')
print(book_price)
