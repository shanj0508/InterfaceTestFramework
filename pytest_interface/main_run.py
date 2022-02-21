# -*- coding: utf-8 -*-
# 入口方法
def run():
    # 指定执行文件
    pytest.main(['-v', './case/test_case03.py', '--alluredir', './result', '--clean-alluredir'])

    os.system('allure serve result')


if __name__ == '__main__':
    run()
