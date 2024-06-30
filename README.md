# 这是基于pytest的接口自动化测试

## 如何开展接口自动化测试？
1、选取自动化测试用例

2、搭建自动化测试环境

3、搭建自动化测试框架

4、代码实现自动化

5、输出测试报告

6、实现持续集成

## 目录结构
- api：封装接口信息
- script：编写测试脚本
- data：存放测试数据
- report：存放测试报告
- common：存放通用工具类
- config.py：定义项目配置信息
- pytest.ini：pytest配置文件

## 使用Pycharm运行
pip install pytest

![image](https://github.com/Peiqi00/Interface-testing/assets/56538770/dbf1c2a1-b907-4fa8-a5dd-ee59b694a440)
![image](https://github.com/Peiqi00/Interface-testing/assets/56538770/fac83163-63a9-4416-bf81-9779a85fcc36)
![image](https://github.com/Peiqi00/Interface-testing/assets/56538770/0873bb28-f3bd-45be-8adc-9654e2c15d60)

## 生成Allure报告
pip install allure-pytest

电脑上安装allure

配置pytest.ini文件

在项目文件夹下运行命令产生测试结果json文件：pytest

在终端运行命令生成测试报告：allure serve report
