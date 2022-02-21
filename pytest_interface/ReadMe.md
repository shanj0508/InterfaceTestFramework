# pytest_interface

## 0.0.1(2022-02-21)

- 框架组成：pytest+requests+allure
- 设计模式：
  - 关键字驱动
- 项目结构：
  - 工具层：api_keyword/
  - 参数层：params/
  - 用例层：case/
  - 数据驱动：data_driver/
  - 数据层：data/
  - 根目录：
    - requirements.txt：环境安装依赖
      - selenium: Web UI自动化测试库
      - pytest: Python第三方单元测试库
      - pytest-rerunfailures: Pytest扩展插件，实现测试用例失败重跑
      - 安装方式：pip install -r requirements.txt